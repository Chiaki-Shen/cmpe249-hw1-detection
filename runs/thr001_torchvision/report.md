# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.492 | 0.236 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.752 | 0.437 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | +0.256 |

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
