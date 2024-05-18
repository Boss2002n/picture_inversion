import cv2
from pathlib import Path
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the current directory as the working directory
os.chdir(current_dir)

# Get the path to the image
img_path = Path("./test_pic.jpeg")

# Check if the image file exists
if not img_path.exists():
    print("Image file not found.")
    exit(1)

# Read the image
image = cv2.imread(str(img_path))

# Convert BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image inversion
inverted_image = 255 - gray_image

# Blur the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred = 255 - blurred

# Perform pencil sketch transformation
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Display the original and pencil sketch images
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
