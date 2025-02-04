# Curved Lines Detection

This repository contains a Python program designed to detect curved parallel lines in an image, identify their center point, and determine the direction of travel. The program processes an input image, calculates intersections, and overlays arrows indicating the direction of travel. It uses advanced image processing techniques and libraries such as OpenCV and NumPy.

## Features

- **Curved Line Detection**  
  Processes images to detect curved parallel lines using Hough Line Transform and clustering techniques.

- **Intersection Calculation**  
  Identifies the intersection points of detected lines and calculates the average center point.

- **Direction Indication**  
  Overlays arrows on the processed image to indicate the direction of travel based on the detected center point.

- **Mouse Interaction (Optional)**  
  Allows users to click on an image to display pixel coordinates or RGB values for debugging purposes.

## File Descriptions

- **curve.py**  
  The main script that:
  - Processes an input image to detect curved lines.
  - Uses Hough Line Transform for line detection.
  - Clusters detected lines into groups using k-means clustering.
  - Calculates intersections of line groups to find the center point.
  - Overlays arrows indicating the direction of travel on the processed image.

- **coordinates.py**  
  A utility script that:
  - Displays an input image.
  - Allows users to click on points in the image to display their pixel coordinates or RGB values.
  - Useful for debugging and understanding pixel-level details in an image.

- **README.md**  
  Provides an overview of the project, its features, file descriptions, and usage instructions.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Curved-Lines-Detection.git
cd Curved-Lines-Detection
2. Install the required Python libraries:
pip install numpy opencv-python
3. To process an image:
- Run `curve.py` with the path to your image file:
  ```
  python curve.py --image path/to/your/image.jpg
  ```
- View the processed image with arrows indicating the direction of travel.

4. To interact with an image:
- Run `coordinates.py`:
  ```
  python coordinates.py
  ```
- Click on any point in the displayed image to view its pixel coordinates or RGB values.

5. Modify or extend functionality by editing the provided Python scripts as needed.

## Libraries Used

- **OpenCV**: For image processing, line detection, and transformations.
- **NumPy**: For numerical operations and array manipulations.
- **argparse**: For command-line argument parsing.

## Notes

This project demonstrates advanced image processing techniques using Python's OpenCV library. It is designed for detecting curved parallel lines in images and determining the direction of travel based on their intersections.
