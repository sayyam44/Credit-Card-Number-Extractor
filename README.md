# Credit Card Number Extraction Using Digital Image Processing

This project was developed as part of **ENGI 9804 - Industrial Machine Vision** and focuses on extracting credit card numbers from images using digital image processing techniques. The implementation relies on Python and the OpenCV library to achieve accurate results without the use of machine learning, making it suitable for devices with limited computational resources. The extraction process involves identifying and processing the credit card number using techniques such as resizing, smoothing, sharpening, and adaptive thresholding. This approach ensures that the project remains compatible with resource-constrained devices while accurately extracting card details.

## Methodology
The methodology involves the following steps:

1. **Image Resizing**: Resizing the input image to 500x315 pixels to standardize the resolution and maintain the aspect ratio.
2. **Grayscale Conversion**: Simplifying the image to make processing efficient.
3. **Image Smoothing**: Reducing noise using a 3x3 averaging kernel.
4. **Edge Detection**: Highlighting important features using Sobel filters.
5. **Adaptive Thresholding**: Binarizing the image for contour detection, adapting to lighting variations.
6. **Image Segmentation**: Identifying contours using OpenCV's `findContours()` function.
7. **Contour Filtering**: Extracting contours likely to represent digits based on their size.
8. **Digit Contour Identification**: Filtering contours based on card number properties, such as alignment and size.
9. **Region of Interest Extraction**: Isolating the part of the image containing the credit card number.

## Output

The script should display five images as output, each showing a different stage of processing. Here's what you should see:

1. **Threshold Image**:
   Displays the binarized image after applying adaptive thresholding. This highlights edges and contrasts features of the card.
   ![Threshold image](https://github.com/user-attachments/assets/aeae7823-ada5-4490-9e87-f1237bedc0c1)

2. **Detected Contours**:
   Shows the original image with all detected contours outlined in blue.
![Detected Contours](https://github.com/user-attachments/assets/d18be55b-15a8-4923-91ec-2285c80d17dd)


3. **Filtered Contours**:
   Displays contours that potentially represent credit card digits (filtered by size) outlined in green.
![Filtered Contours](https://github.com/user-attachments/assets/626c2bb2-c3f3-4ba2-b779-0e7a39d0be03)


4. **ROI (Region of Interest)**:
   Highlights the bounding box around the detected credit card number on the original image.
![ROI (Region of Interest)](https://github.com/user-attachments/assets/d497d360-d4d9-44c2-927a-67151d62e207)

5. **Extracted Number**:
   Shows only the cropped portion of the image containing the detected card number.
![Extracted Number](https://github.com/user-attachments/assets/0a379a07-1c26-4bf9-9065-212a8a6b4da2)


## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Usage

To run the script, simply call the `getCardNumber(image)` function and pass an image to it. Ensure that the image file is accessible and has a valid path.

Example:
```python
image = cv2.imread('Black.jpg')
getCardNumber(image)
