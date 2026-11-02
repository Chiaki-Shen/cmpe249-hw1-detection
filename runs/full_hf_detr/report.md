# ngdet evaluation report

Unified taxonomy: **driving3** = `['vehicle', 'person', 'cyclist']`

## Summary matrix — mAP @[.5:.95]

| model \ dataset | coco | kitti |
|---|---|---|
| hf_detr:PekingU/rtdetr_r50vd | 0.492 | 0.239 |

## Summary matrix — AP50

| model \ dataset | coco | kitti |
|---|---|---|
| hf_detr:PekingU/rtdetr_r50vd | 0.709 | 0.437 |

## Generalization gap (COCO mAP − driving-dataset mAP)

Positive = drop when moving from the COCO training domain to a driving domain (higher = worse generalization).

| model | kitti |
|---|---|
| hf_detr:PekingU/rtdetr_r50vd | +0.253 |

## Full COCO tables (per run)

### hf_detr:PekingU/rtdetr_r50vd  ×  coco  (5000 imgs, 235.7s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.492 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.709 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.518 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.241 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.504 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.704 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.232 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.536 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.567 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.330 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.599 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.762 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.537 |
| person | 0.570 |
| cyclist | 0.369 |

### hf_detr:PekingU/rtdetr_r50vd  ×  kitti  (5984 imgs, 319.5s, open_vocab=False)

| Metric | Value |
|---|---|
| AP  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.239 |
| AP  @[IoU=0.50      | area=   all | maxDets=100] | 0.437 |
| AP  @[IoU=0.75      | area=   all | maxDets=100] | 0.234 |
| AP  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.129 |
| AP  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.227 |
| AP  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.314 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=  1] | 0.105 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets= 10] | 0.299 |
| AR  @[IoU=0.50:0.95 | area=   all | maxDets=100] | 0.309 |
| AR  @[IoU=0.50:0.95 | area= small | maxDets=100] | 0.245 |
| AR  @[IoU=0.50:0.95 | area=medium | maxDets=100] | 0.306 |
| AR  @[IoU=0.50:0.95 | area= large | maxDets=100] | 0.371 |

| Class | AP@[.5:.95] |
|---|---|
| vehicle | 0.482 |
| person | 0.232 |
| cyclist | 0.002 |
