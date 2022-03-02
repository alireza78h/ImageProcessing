import cv2 as cv
imagePath=r"F:\\Semester 8\\IMP\\HW1\\ImageProcessing\\HW1\\campusdrive.png"
img = cv.imread(imagePath)
print("Image bit depth is : "+str(img.dtype)[-1])