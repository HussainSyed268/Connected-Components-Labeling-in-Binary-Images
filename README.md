# Connected-Components-Labeling-in-Binary-Images
This project is an implementation of connected components labeling in binary images using a two-pass algorithm with 8-connectivity. It labels objects in a binary image and assigns distinct colors to each labeled region.

## Introduction

Connected components labeling is a fundamental image processing task that is used to identify and label distinct objects or regions in a binary image. This project provides a Python implementation of this task using a two-pass algorithm with 8-connectivity, allowing you to label and color objects in a binary image.

## Prerequisites

- Python
- OpenCV (cv2) library

## Working

The input image must be a Binary Image. In this case a Binary Image with 8 white crosses against a black background was used.

![Screenshot from 2023-10-24 22-23-35](https://github.com/HussainSyed268/Connected-Components-Labeling-in-Binary-Images/assets/100157373/95791e26-caec-47c7-aa60-3b9a37446cc0)


The output image would be an RGB Image labeling and coloring the objects in the Binary Image. This was done using the two-pass algorithm with 8-connectivity

![Screenshot from 2023-10-24 22-25-21](https://github.com/HussainSyed268/Connected-Components-Labeling-in-Binary-Images/assets/100157373/2e58a771-d0d3-49b9-9fc5-aaea6f0abc2d)

## Code Explanation

The code implements a two-pass algorithm for connected components labeling with 8-connectivity. It assigns labels to objects in the input binary image and assigns colors to the labels. The main steps include:

- Thresholding the grayscale image to create a binary image.
- First pass: Labeling vertically close pixels using a two-pass approach.
- Second pass: Labeling horizontally close pixels in the same object.
- Assigning distinct colors to each label.
- Displaying the labeled image and the colored result.

