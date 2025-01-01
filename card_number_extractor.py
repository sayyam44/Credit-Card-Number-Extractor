import cv2
import numpy as np
import os

def getCardNumber(image):
    if image is None:
        print("Error: Image not found or cannot be loaded!")
        return

    # Re-sizing image to 500x315 to standardize captured card's size
    image = cv2.resize(image, (500, 315))

    # Converting image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3x3 averaging kernel and smoothing operation
    kernel = np.ones((3, 3), np.float32) / 9
    smooth_img = cv2.filter2D(gray, -1, kernel)

    # 3x3 Sobel filters and sharpening operation
    sobelx = cv2.Sobel(smooth_img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(smooth_img, cv2.CV_64F, 0, 1, ksize=3)
    grad = np.sqrt(sobelx**2 + sobely**2)
    sharpened_img = (grad * 255 / grad.max()).astype(np.uint8)

    # Using adaptive thresholding to contrast and highlight card's features
    thresh = cv2.adaptiveThreshold(
        sharpened_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Image segmentation using contour detection
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Making different copies of the image to highlight detected contours
    image_contours = image.copy()
    image_filtered_contours = image.copy()
    image_extracted_roi = image.copy()

    filtered_cnts = []
    contour_y = []
    for contour in cnts:
        x, y, w, h = cv2.boundingRect(contour)
        # Highlighting all detected contours in blue color
        cv2.rectangle(image_contours, (x, y), (x + w, y + h), (255, 0, 0), 1)

        # Filtering potential credit card digits with size (Width: 10-30 px; Height: 10-60 px)
        if 10 <= w <= 30 and 10 <= h <= 60:
            # Highlighting possible credit card digits in green color
            cv2.rectangle(image_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)
            filtered_cnts.append(contour)
            contour_y.append(y)

    # Credit card number will have maximum contours in a single row.
    # Extracting 'y' value with the maximum number of contours
    if not contour_y:
        print("No potential credit card digits detected.")
        return

    mode_y = max(set(contour_y), key=contour_y.count)

    contour_x, contour_w, contour_h = [], [], []
    for contour in filtered_cnts:
        x, y, w, h = cv2.boundingRect(contour)
        # Select all contours that are within 5 px of mode_y
        if mode_y - 5 < y < mode_y + 5:
            contour_x.append(x)
            contour_w.append(w)
            contour_h.append(h)
            # Highlighting all such contours in green color
            cv2.rectangle(image_filtered_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if not contour_x:
        print("No contours found in the mode row.")
        return

    # Determining ROI/bounding box for all contours belonging to the card number
    roi_x = min(contour_x)
    roi_y = mode_y
    roi_w = max(contour_x) + max(contour_w) - roi_x
    roi_h = max(contour_h)

    # Highlighting the card number's location in the image
    cv2.rectangle(image_extracted_roi, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (0, 255, 0), 2)

    # Extracting the card number from the image
    extracted_number = image[roi_y : roi_y + roi_h, roi_x : roi_x + roi_w]

    # Displaying various stages of processing
    cv2.imshow("Threshold Image", thresh)
    cv2.imshow("Detected Contours", image_contours)
    cv2.imshow("Filtered Contours", image_filtered_contours)
    cv2.imshow("ROI", image_extracted_roi)
    cv2.imshow("Extracted Number", extracted_number)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the image
file_path = "Black.jpg"
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found in the current directory.")
else:
    image = cv2.imread(file_path)
    getCardNumber(image)
