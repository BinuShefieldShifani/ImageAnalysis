import cv2 as cv
import sys
import numpy as np
img = cv.imread(cv.samples.findFile("img.tif")) 
mod_img=img
if img is None:
  sys.exit("Could not read the image.") 
else:
    rows, cols, channels = mod_img.shape  # .shape gives (rows, cols, channels)
    img_dtype = mod_img.dtype             # .dtype gives data type of image

    # Print the properties
    print(f"Number of rows (height): {rows}")
    print(f"Number of columns (width): {cols}")
    print(f"Number of channels: {channels}")
    print(f"Image data type: {img_dtype}")
    # Access the value of the first pixel (top-left corner at (0, 0))
    valuePix1 = mod_img[0, 0]
    print(f"Original value of the first pixel (0,0): {valuePix1}")

    # Modify the value of the first pixel
    new_value = [255, 0, 0]  # Example: Set to blue color if the image is in color (BGR format)
    mod_img[0, 0] = new_value
    print("Modified value at (0, 0):", mod_img[0, 0])
    print(f"New value of the first pixel (0,0): {mod_img[0, 0]}")
    
    # Define a Region of Interest (ROI)
    # Selecting a 50x50 pixels area starting from (50,50) to (100,100)
    ROI = mod_img[50:100, 50:100]
    
    # Check the shape of the ROI
    print(f"ROI shape: {ROI.shape}")
    print("Original value of ROI pixel (0, 0):", ROI[0, 0])
    ROI[0, 0] = [0, 0, 255]
    print("Modified value of ROI pixel (0, 0):", ROI[0, 0])
    
mod_img[0:50, 0:50] = [255, 0, 0]
difference = cv.absdiff(img,mod_img)

# Count non-zero pixels in the difference image (these represent changes)
changes_count = np.count_nonzero(difference)

if changes_count > 0:
    print(f"Number of changed pixels: {changes_count}")
else:
    print("No changes detected.")

cv.imshow("Display window", mod_img)
k = cv.waitKey(0)
if k == ord("s"):
  cv.imwrite("savedImg.tif", img)

