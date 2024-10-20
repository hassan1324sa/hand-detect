# Hand Gesture Volume Control

This project enables control of system volume using hand gestures captured by a webcam. It utilizes OpenCV for video processing, MediaPipe for hand tracking, and pynput to simulate volume control key presses.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

- Real-time hand tracking using MediaPipe.
- Volume control based on the distance between the index and pinky fingers.
- Visual feedback with hand landmarks and a dynamic volume bar.

## Requirements

Before running the script, ensure you have the following Python packages installed:

```bash
pip install opencv-python mediapipe pynput numpy
