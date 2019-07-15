import pytesseract
import argparse
import cv2
import os

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

print('x resized by {} and y by {}'.format(fx,fy))
print("------------")

for filename in os.listdir(args["imageDir"]):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image = cv2.imread(os.path.join(args["imageDir"], filename))
        # to resize
        if args["resize"]:
            image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if args["preprocess"] == "thresh":
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        text = pytesseract.image_to_string(gray)

        print(image.shape)
        print(filename)
        print(text)
        print("------------")