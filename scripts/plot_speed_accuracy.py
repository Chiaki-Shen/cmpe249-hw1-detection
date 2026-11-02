# Speed vs accuracy plot for CMPE 249 HW (RTX 2070, batch 1, KITTI image 000008.png)
# mAP: runs/thr001_*/metrics.json (score-thr 0.001)
# FPS: runs/latency_*/latency_report.md (warmup 5, iters 50)
import matplotlib.pyplot as plt

models = {
    #  name           COCO   KITTI  FPS32  FPS16  peak MiB (minus 314 idle)
    "Faster R-CNN": (0.492, 0.236, 13.7, 24.0, 1299),
    "YOLO11x":      (0.558, 0.239, 50.7, 53.7, 653),
    "RT-DETR-R50":  (0.517, 0.243, 23.9, 32.4, 633),
}

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)
for ax, idx, title in [(axes[0], 0, "COCO val2017"), (axes[1], 1, "KITTI (zero-shot)")]:
    for name, v in models.items():
        acc = v[idx]
        ax.plot([v[2], v[3]], [acc, acc], "-", color="gray", lw=1)          # fp32 -> fp16 line
        ax.scatter(v[2], acc, s=v[4] / 4, facecolors="none", edgecolors="k")  # fp32: hollow
        ax.scatter(v[3], acc, s=v[4] / 4, label=name)                         # fp16: filled
        ax.annotate(name, (v[3], acc), textcoords="offset points", xytext=(6, 6), fontsize=9)
    ax.set_title(title)
    ax.set_xlabel("FPS on RTX 2070 (hollow = fp32, filled = fp16)")
    ax.set_ylabel("mAP@[.5:.95]")
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 0.6)
fig.suptitle("Speed vs accuracy (marker size = peak GPU memory)")
fig.tight_layout()
out = "/home/" + __import__("getpass").getuser() + "/cmpe249-hw/notes/figures/speed_vs_accuracy.png"
fig.savefig(out, dpi=150)
print("saved", out)
