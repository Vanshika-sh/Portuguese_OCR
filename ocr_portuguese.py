from textblob import TextBlob
from pytesseract import image_to_string
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-l", "--lang", required=True,
	help="language that Tesseract will use when OCR'ing")
ap.add_argument("-t", "--to", type=str, default="en",
	help="language that we'll be translating to")
ap.add_argument("-p", "--psm", type=int, default=1,
	help="Tesseract PSM mode")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Image",rgb)
options = "-l {} --psm {}".format(args["lang"], args["psm"])
text = image_to_string(rgb, config=options)
print("ORIGINAL")
print("========")
print(text)
print("")

file = open("text_file","w")
file.write(text)
print(text)

tb = TextBlob(text)
translated = tb.translate(to=args["to"])

print("TRANSLATED")
print("==========")
print(translated)
ts = str(translated)

file = open("ts","w")
file.write(ts)
print(ts)
