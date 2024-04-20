# Pothole Detection using YOLOv8s

## Overview

This project aims to detect potholes in video frames using YOLOv8s. Each frame from the video has been annotated to indicate the presence of a pothole, making it a valuable resource for understanding pothole distribution and aiding road maintenance or safety measures.

## Objectives

- Detect potholes in video frames using YOLOv8s.
- Serve as a learning resource for beginners to understand YOLO model training with video data.

## Installation

To install YOLOv8s, use the following pip command:

```bash
pip install ultralytics
```
## Dataset Details

- **Source**: Video dataset (MP4)
- **Annotation**: Each frame from the video has been annotated to indicate pothole presence.
- **Format**: JPG (Images) & Text Document (Labels)

### Columns

- **Frame Number**: Identifier for each frame.
- **Pothole Presence**: Binary indicator (1 if pothole is present, 0 otherwise).
- **Location**: Latitude and Longitude of the pothole.

## Usage

### Data Preparation:

1. Extract frames from the video.
2. Use the annotated CSV for training and testing.

### YOLOv8s Training:

1. Utilize Roboflow for manual annotation using polygon markers.
2. Train the YOLOv8s model on the annotated frames.

## Contributing

We welcome contributions! Please refer to the [Contribution Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
