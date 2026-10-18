import cv2
import os

folder = "data/real"
files = os.listdir(folder)
print("Number of images:", len(files))
print("First file:", files[0])

img = cv2.imread(os.path.join(folder, files[0]), cv2.IMREAD_GRAYSCALE)
print("Shape (height, width):", img.shape)

cv2.imshow("print", img)
cv2.waitKey(0)
cv2.destroyAllWindows()