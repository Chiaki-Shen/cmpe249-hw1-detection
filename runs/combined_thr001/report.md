# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.492 | 0.236 |
| yolo:yolo11x.pt | 0.558 | 0.239 |
| hf_detr:PekingU/rtdetr_r50vd | 0.517 | 0.243 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.752 | 0.437 |
| yolo:yolo11x.pt | 0.773 | 0.444 |
| hf_detr:PekingU/rtdetr_r50vd | 0.754 | 0.449 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | +0.256 |
| yolo:yolo11x.pt | +0.319 |
| hf_detr:PekingU/rtdetr_r50vd | +0.274 |

## Full COCO tables (per run)

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  coco  (5000 imgs, 515.6s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.492 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.752 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.523 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.286 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.500 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.660 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.232 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.553 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.606 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.438 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.629 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.745 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.531 |
| person | 0.565 |
| cyclist | 0.379 |

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  kitti  (5984 imgs, 522.5s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.236 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.437 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.235 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.120 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.231 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.312 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.110 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.316 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.341 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.318 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.334 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.378 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.451 |
| person | 0.256 |
| cyclist | 0.001 |

### yolo:yolo11x.pt  ×  coco  (5000 imgs, 198.4s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.558 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.773 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.606 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.295 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.583 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.755 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.255 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.612 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.681 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.468 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.734 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.826 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.595 |
| person | 0.627 |
| cyclist | 0.451 |

### yolo:yolo11x.pt  ×  kitti  (5984 imgs, 198.4s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.239 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.444 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.236 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.135 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.230 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.311 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.108 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.314 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.342 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.284 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.346 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.383 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.474 |
| person | 0.243 |
| cyclist | 0.001 |

### hf_detr:PekingU/rtdetr_r50vd  ×  coco  (5000 imgs, 253.7s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.517 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.754 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.542 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.266 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.527 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.726 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.237 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.576 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.671 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.488 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.687 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.833 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.563 |
| person | 0.593 |
| cyclist | 0.395 |

### hf_detr:PekingU/rtdetr_r50vd  ×  kitti  (5984 imgs, 371.9s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.243 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.449 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.237 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.131 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.234 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.323 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.108 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.320 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.361 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.323 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.355 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.400 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.490 |
| person | 0.239 |
| cyclist | 0.002 |
