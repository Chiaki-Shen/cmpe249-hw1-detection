# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.481 | 0.234 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | 0.731 | 0.432 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| torchvision:fasterrcnn_resnet50_fpn_v2 | +0.246 |

## Full COCO tables (per run)

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  coco  (5000 imgs, 520.2s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.481 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.731 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.514 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.276 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.489 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.650 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.230 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.534 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.570 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.391 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.596 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.716 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.520 |
| person | 0.554 |
| cyclist | 0.368 |

### torchvision:fasterrcnn_resnet50_fpn_v2  ×  kitti  (5984 imgs, 522.3s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.234 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.432 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.233 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.120 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.227 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.308 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.109 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.312 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.328 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.304 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.320 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.368 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.447 |
| person | 0.255 |
| cyclist | 0.001 |
