# 🖼️ Image Analysis & Computer Vision Experiments

A collection of computer vision and image processing scripts covering classical techniques, real-time detection, deep learning, and ArUco-based spatial measurement — written as part of coursework and personal exploration.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?logo=tensorflow)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-blue?logo=numpy)

---

## 📁 File Overview

### 🔬 Image Processing Fundamentals

| File | Description |
|---|---|
| `exercise1.py` | Loads an image and extracts key properties — height, width, channels, data type, mean/max/min intensity, aspect ratio, and memory contiguity |
| `exercise2.py` | Reads pixel RGB values at specific coordinates and marks them visually on the image |
| `exercise3.py` | Interactive dynamic thresholding using OpenCV trackbars — demonstrates all 5 threshold types (Binary, Binary Inv, Trunc, ToZero, ToZero Inv) side by side |
| `exercise4.py` | Splits a colour image into its BGR channels and visualises each channel both in grayscale and colour |
| `exercise5.py` | Real-time contour detection using Canny edge detection with interactive trackbar controls for lower/upper thresholds and minimum contour area |
| `exercise6.py` | Centroid detection of objects using both Canny edge detection and binarization — compares results from both methods and marks the centroid |
| `exercise7.py` | Object orientation estimation using `minAreaRect` — compares orientation angles computed via Canny vs binarization |

---

### 🏷️ ArUco Marker Detection & Spatial Measurement

| File | Description |
|---|---|
| `MainArucoDetection.py` | Real-time ArUco marker detection from webcam feed — computes pixel-to-cm ratio from a detected marker and measures object dimensions (credit card, AAA battery) using binarization-based contour detection |
| `MachineVision.py` | ArUco-based real-time object measurement — calculates pixel-to-pixel ratio from marker width and draws bounding boxes with dimensions for objects of known size ranges |
| `mask.py` | ArUco-guided video masking — detects marker in a video, computes pixels-per-mm scale, and applies a precisely sized mask at a real-world offset below the marker. Supports configurable object dimensions, span, and horizontal offset in mm |

---

### 🧪 Detection Utilities

| File | Description |
|---|---|
| `MyDetectionMethods.py` | Reusable utility class with static methods for image preprocessing (grayscale + Gaussian blur), Canny-based contour detection, and binarization-based contour detection |
| `MyDetectionMethods2.py` | Updated version of `MyDetectionMethods.py` with the same interface — used as an interchangeable drop-in replacement |

---

### 🪡 Needle Detection with ArUco Calibration

| File | Description |
|---|---|
| `MachineVisionProjectFinal.py` | Real-time sewing needle detection and classification using ArUco calibration — detects needle length in mm, identifies needle head colour (Red, Blue, Green, Yellow, Black, White) using HSV colour analysis, and counts needles per frame |

---

### 🤖 Deep Learning (TensorFlow / Keras)

| File | Description |
|---|---|
| `Lab1_DU.py` | NumPy tensor operations — element-wise addition/multiplication, reshaping, slicing, concatenation, splitting, and basic statistics. Also includes a simple dense neural network definition using Keras Sequential API |
| `Lab6.py` | Neural network experiments on MNIST (digit classification, 97.4% test accuracy) and IMDB (sentiment classification) datasets, plus CNN implementation on CIFAR-10 (70% test accuracy) with data augmentation using `ImageDataGenerator` |

---

### 🔧 Sensor & Lab Exercises

| File | Description |
|---|---|
| `Sensor_Lab1.py` | Pixel manipulation fundamentals — reading image properties, modifying individual pixel values, defining ROIs, and comparing original vs modified images using `cv2.absdiff` |
| `sensorLab4.py` | Sensor lab exercise 4 |
| `sensorLab5.py` | Sensor lab exercise 5 |

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Computer Vision | OpenCV 4.x (`cv2`) |
| Deep Learning | TensorFlow / Keras |
| Numerical Computing | NumPy |
| ArUco Markers | `cv2.aruco` module |
| Datasets | MNIST, CIFAR-10, IMDB (via Keras) |

---

## ▶️ Running the Scripts

### Prerequisites

```bash
pip install opencv-python opencv-contrib-python numpy tensorflow matplotlib
```

> `opencv-contrib-python` is required for ArUco marker support.

### Scripts with live camera feed

The following scripts open your webcam and run until you press `q`:

- `MainArucoDetection.py`
- `MachineVision.py`
- `MachineVisionProjectFinal.py`

### Scripts with trackbar controls

The following scripts open an OpenCV window with interactive sliders:

- `exercise3.py` — threshold controls
- `exercise5.py` — Canny and area controls

### Image-based scripts

All `exercise*.py` and `Sensor_Lab*.py` scripts expect image files in a local directory. Update the `os.chdir()` path and image filename at the top of each script to match your setup before running.

---

## 👤 Author

**Binu Shefield Shifani**
Software Engineer (5 years, Cognizant Technology Solutions)
MS AI & Automation · University West, Trollhättan, Sweden

[![GitHub](https://img.shields.io/badge/GitHub-BinuShefieldShifani-black?logo=github)](https://github.com/BinuShefieldShifani)
