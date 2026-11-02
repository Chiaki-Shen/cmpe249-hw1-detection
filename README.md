# CMPE 249 HW1: Zero-shot 2D object detection, COCO to KITTI

Track A. Three COCO-pretrained detectors evaluated with the course's ngdet toolkit
(DeepDataMiningLearning, commit bed852ddbcabab7febef0b596e7fbd78cf5b197d):
Faster R-CNN v2 (torchvision), YOLO11x (Ultralytics), RT-DETR-R50 (Hugging Face).
Datasets: COCO val2017 (5,000 images) and KITTI 2D (5,984-image "train" part of ngdet's seed-42 split, zero-shot).

## Contents
- `notes/commands.log`: every command run, in order (S1 to S14)
- `notes/env.txt`: GPU, driver, pip freeze, ngdet commit
- `runs/thr001_*`: main results (score threshold 0.001); `runs/full_*`: threshold 0.3 sensitivity runs; `runs/smoke`: 50-image smoke test
- `runs/latency_*.log`, `runs/mem_*.txt`: latency (fp32 / fp16 / compile) and GPU memory sampling
- `runs/combined_thr001/`: merged report and heatmap
- `scripts/inspect_frame.py`: per-box predictions vs KITTI labels for one image (re-runs each library directly with the same checkpoints, threshold 0.3; not through ngdet's adapters)
- `scripts/plot_speed_accuracy.py`: speed vs accuracy figure
- `notes/frame*_inspect.txt`: outputs of inspect_frame.py used for the failure-analysis slides

Not included: datasets, model weights, prediction JSON files, videos and frame dumps.

Hardware: RTX 2070 8 GB, Ryzen 5 2600X, Ubuntu 22.04.5, Python 3.10.12, torch 2.14.1+cu126.
