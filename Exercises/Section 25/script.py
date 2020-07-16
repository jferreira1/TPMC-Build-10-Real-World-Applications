import cv2
import os

pathname = r".\The Python Mega Course\Exercises\Section 25\images"
img_list = os.scandir(pathname)
for entry in img_list:
    fullpath = os.path.join(pathname, entry.name)
    img = cv2.imread(fullpath, 0)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imwrite(os.path.splitext(fullpath)[0] + "_resized.jpg", resized_img)
