# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.477 | 0.251 |
| yolo:yolo11x.pt | 0.399 | 0.247 |
| hf_detr:PekingU/rtdetr_r50vd | 0.532 | 0.246 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.640 | 0.465 |
| yolo:yolo11x.pt | 0.486 | 0.426 |
| hf_detr:PekingU/rtdetr_r50vd | 0.682 | 0.437 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | +0.226 |
| yolo:yolo11x.pt | +0.151 |
| hf_detr:PekingU/rtdetr_r50vd | +0.286 |

## Full COCO tables (per run)

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  coco  (50 imgs, 19.0s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.477 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.640 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.569 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.377 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.659 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.736 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.359 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.649 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.684 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.493 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.739 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.764 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.622 |
| person | 0.576 |
| cyclist | 0.233 |

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  kitti  (50 imgs, 5.3s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.251 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.465 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.231 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.177 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.245 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.321 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.080 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.282 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.309 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.315 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.293 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.350 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.465 |
| person | 0.287 |
| cyclist | 0.000 |

### yolo:yolo11x.pt  ×  coco  (50 imgs, 26.0s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.399 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.486 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.441 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.297 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.485 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.757 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.130 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.407 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.417 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.327 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.516 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.771 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.633 |
| person | 0.564 |
| cyclist | 0.000 |

### yolo:yolo11x.pt  ×  kitti  (50 imgs, 2.2s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.247 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.426 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.245 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.147 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.233 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.345 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.090 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.278 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.289 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.225 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.276 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.369 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.468 |
| person | 0.274 |
| cyclist | 0.000 |

### hf_detr:PekingU/rtdetr_r50vd  ×  coco  (50 imgs, 26.7s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.532 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.682 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.602 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.321 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.623 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.750 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.129 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.677 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.695 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.366 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.806 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.767 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.607 |
| person | 0.589 |
| cyclist | 0.400 |

### hf_detr:PekingU/rtdetr_r50vd  ×  kitti  (50 imgs, 3.6s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.246 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.437 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.221 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.146 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.235 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.331 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.081 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.276 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.301 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.282 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.284 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.356 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.494 |
| person | 0.243 |
| cyclist | 0.000 |
