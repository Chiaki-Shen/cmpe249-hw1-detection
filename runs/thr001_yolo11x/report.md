# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| yolo:yolo11x.pt | 0.558 | 0.239 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| yolo:yolo11x.pt | 0.773 | 0.444 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| yolo:yolo11x.pt | +0.319 |

## Full COCO tables (per run)

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
