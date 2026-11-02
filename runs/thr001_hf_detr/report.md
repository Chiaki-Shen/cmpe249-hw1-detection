# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| hf_detr:PekingU/rtdetr_r50vd | 0.517 | 0.243 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| hf_detr:PekingU/rtdetr_r50vd | 0.754 | 0.449 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| hf_detr:PekingU/rtdetr_r50vd | +0.274 |

## Full COCO tables (per run)

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
