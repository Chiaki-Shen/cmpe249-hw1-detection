import torch
from PIL import Image

KITTI = "/home/a/cmpe249-hw/datasets/kitti/training"
import sys
ID = sys.argv[1] if len(sys.argv) > 1 else "005663"
IMG = f"{KITTI}/image_2/{ID}.png"
THR = 0.3                           # same threshold as the video frames
dev = "cuda"

# ground truth from the KITTI label file
gt = []
for line in open(f"{KITTI}/label_2/{ID}.txt"):
    p = line.split()
    gt.append((p[0], [float(v) for v in p[4:8]]))

def iou(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = ix * iy
    area = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / (area(a) + area(b) - inter + 1e-9)

# driving3 fold, same names as ngdet taxonomy.py
FOLD = {"car": "vehicle", "truck": "vehicle", "bus": "vehicle", "train": "vehicle",
        "motorcycle": "vehicle", "motorbike": "vehicle", "person": "person", "bicycle": "cyclist"}

def report(name, dets):
    print(f"\n=== {name}: {len(dets)} predictions >= {THR} ===")
    print(f"{'native':12} {'unified':10} {'score':>5}  {'box x1,y1,x2,y2':22} best GT (IoU)")
    for cls, s, b in sorted(dets, key=lambda d: d[2][0]):
        g = max(gt, key=lambda t: iou(b, t[1]))
        v = iou(b, g[1])
        best = f"{g[0]} {v:.2f}" if v > 0 else "none"
        box = ",".join(str(int(x)) for x in b)
        print(f"{cls:12} {FOLD.get(cls, '(dropped)'):10} {s:5.2f}  {box:22} {best}")

img = Image.open(IMG).convert("RGB")

# YOLO11x
from ultralytics import YOLO
r = YOLO("yolo11x.pt")(IMG, conf=THR, verbose=False)[0]
report("YOLO11x", [(r.names[int(c)], float(s), b.tolist())
                   for b, s, c in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls)])

# Faster R-CNN v2 (COCO_V1)
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights as W
from torchvision.transforms.functional import to_tensor
w = W.DEFAULT
m = fasterrcnn_resnet50_fpn_v2(weights=w).eval().to(dev)
with torch.no_grad():
    o = m([to_tensor(img).to(dev)])[0]
cats = w.meta["categories"]
report("Faster R-CNN", [(cats[int(l)], float(s), b.tolist())
                        for b, s, l in zip(o["boxes"], o["scores"], o["labels"]) if s >= THR])

# RT-DETR-R50
from transformers import AutoImageProcessor, AutoModelForObjectDetection
proc = AutoImageProcessor.from_pretrained("PekingU/rtdetr_r50vd")
mdl = AutoModelForObjectDetection.from_pretrained("PekingU/rtdetr_r50vd").eval().to(dev)
inp = proc(images=img, return_tensors="pt").to(dev)
with torch.no_grad():
    out = mdl(**inp)
res = proc.post_process_object_detection(out, target_sizes=torch.tensor([img.size[::-1]]), threshold=THR)[0]
report("RT-DETR", [(mdl.config.id2label[int(l)], float(s), b.tolist())
                   for s, l, b in zip(res["scores"], res["labels"], res["boxes"])])
