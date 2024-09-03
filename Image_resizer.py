import cv2

# Configurable parameters
source = "ckp.jpg"
destination = "new_Image.jpg"
scale_percent = 40

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)

# Calculating the 50% of the original dimension
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# Resize image
output = cv2.resize(image, (width, height))

cv2.imwrite(destination, output)

cv2.waitKey(0)