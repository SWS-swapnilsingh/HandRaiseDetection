# Real-time Pose Detection using YOLO and OpenCV

This Python script demonstrates real-time pose detection using the YOLO model and OpenCV. It captures frames from the camera, performs pose detection using YOLO, and annotates the frames with detected keypoints.

## Requirements

- Python 3.x
- OpenCV (`cv2` Python package)
- Ultralytics YOLO (`ultralytics` Python package)

Make sure to install the required packages before running the script.

## Code Explanation
In this project, I have used the YOLOv8 pose detection model to detect whether the person standing in front of the camera has raised his hands. If the coordinates of the shoulder are below the coordinates of the elbow then it will say "Hand is raised" otherwise "Hand is not raised"
