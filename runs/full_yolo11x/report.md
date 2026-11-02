# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| yolo:yolo11x.pt | 0.492 | 0.229 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| yolo:yolo11x.pt | 0.661 | 0.418 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| yolo:yolo11x.pt | +0.263 |

## Full COCO tables (per run)

### yolo:yolo11x.pt  ×  coco  (5000 imgs, 188.5s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.492 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.661 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.538 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.230 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.511 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.708 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.243 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.528 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.539 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.277 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.579 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.751 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.531 |
| person | 0.558 |
| cyclist | 0.386 |

### yolo:yolo11x.pt  ×  kitti  (5984 imgs, 187.2s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.229 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.418 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.230 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.128 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.217 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.303 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.106 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.295 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.299 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.224 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.296 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.365 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.457 |
| person | 0.229 |
| cyclist | 0.001 |
