# Digital Image Processing

A collection of assignments and mini-projects exploring the fundamentals of Digital Image Processing (DIP) using Python. This repository documents hands-on implementations of core DIP concepts, starting with image I/O and pixel-level neighborhood relationships.

## 📌 Overview

This repo is structured as a series of assignments, each focused on a specific concept in digital image processing — from reading and displaying images to analyzing pixel relationships and neighborhoods. It's intended as a learning log / portfolio of DIP coursework and experiments.

## 🗂️ Repository Structure
Digital-Image-Processing/
│
├── Assignment 1 - Image reading and Pixel relationship/
│   ├── image.py      # Read and display an image using OpenCV
│   └── pixels.py      # Explore pixel neighborhoods (4-, diagonal, 8-connectivity)
│
└── README.md

## 📖 Assignments

### Assignment 1 — Image Reading and Pixel Relationships

**`image.py`**
Reads an image from disk using OpenCV (`cv2.imread`) and displays it in a window. Includes a basic check for whether the image was loaded successfully (handles the case where the file path is invalid or missing).

```python
import cv2

img = cv2.imread("path/to/image.jpg")

if img is None:
    print("Image was not found!")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

> ⚠️ Note: The image path is currently hardcoded to a local file. Update the path in `image.py` to point to an image on your own machine before running.

**`pixels.py`**
Demonstrates fundamental pixel relationship concepts using a 5×5 NumPy array representing a grayscale image matrix:
- Locates a center pixel and prints its value
- Computes the **4-neighborhood** (N4) — the pixels directly above, below, left, and right
- Computes the **diagonal neighbors** (ND) — the four diagonal pixels
- Computes the **8-neighborhood** (N8) — the union of N4 and ND

This is a foundational concept in DIP used in operations like edge detection, connected component analysis, and morphological processing.

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV** (`cv2`) — image reading, display, and processing
- **NumPy** — matrix/array representation of image data

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 installed, then install the required dependencies:

```bash
pip install opencv-python numpy
```

### Running the scripts

```bash
# Navigate to the assignment folder
cd "Assignment 1 - Image reading and Pixel relationship"

# Run the image display script (update the image path first)
python image.py

# Run the pixel neighborhood script
python pixels.py
```

## 🎯 Goals of This Repository

- Build a strong foundation in core DIP concepts before moving to more advanced topics (filtering, transformations, segmentation, feature extraction, etc.)
- Serve as a reference/portfolio of coursework and self-driven DIP practice
- Progressively add assignments covering topics such as:
  - Image enhancement (histogram equalization, contrast stretching)
  - Spatial filtering (smoothing, sharpening)
  - Frequency domain processing (Fourier transforms)
  - Edge detection (Sobel, Canny)
  - Morphological operations
  - Image segmentation

## 📈 Roadmap

- [x] Assignment 1: Image reading & pixel relationships
- [ ] Assignment 2: TBD
- [ ] Assignment 3: TBD

## 🤝 Contributing

This is a personal learning repository, but suggestions and feedback are welcome via issues or pull requests.

## 📄 License

This project is currently unlicensed. Feel free to reach out if you'd like to use or reference this work.

## 👤 Author

**Veer**
[GitHub](https://github.com/Veer2401)
