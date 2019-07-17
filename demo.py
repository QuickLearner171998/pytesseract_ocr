import pytesseract
import argparse
import cv2
import os
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imageDir", required=True,help="path to input image dir ")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",help="type of preprocessing to be done")
ap.add_argument("-r", "--resize", default=False, help="whether resize needed or not")
args = vars(ap.parse_args())
print('------------')
print('resize={}'.format(args["resize"]))

# resize factors
fx = 1.5
fy = 2.5

if args["resize"]:
    print('x resized by {} and y by {}'.format(fx, fy))
    print("------------")

for filename in os.listdir(args["imageDir"]):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image = cv2.imread(os.path.join(args["imageDir"], filename))
        # to resize
        if args["resize"]:
            image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # gray = cv2.bitwise_not(gray)

        # if args["preprocess"] == "thresh":
        #     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # coords = np.column_stack(np.where(gray>0))
        # angle = cv2.minAreaRect(coords)[-1]
        #
        # if angle < -45:
        #     angle = -(90+angle)
        #
        # else:
        #     angle = -angle
        #
        # (h, w) = gray.shape[:2]
        # center = (w//2 , h//2)
        # M = cv2.getRotationMatrix2D(center, angle, 1.0)
        # rotated = cv2.warpAffine(gray, M, (w,h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        #

        text = pytesseract.image_to_string(gray, config='--psm 7')

        print(image.shape)
        print(filename)
        print(text)
        print("------------")