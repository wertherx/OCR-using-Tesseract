from PIL import Image
import pytesseract
import numpy as np
import cv2 

print ("Welcome to Tesseraact OCR")
fileName = input("Enter the Image File Name: ")

print("Select the image format\n\t1) PNG\n\t2) JPG")
num = int(input(""))

if(num == 1):
    fileName += ".png"
elif (num == 2):
    fileName += ".jpg"

print("-----------------")
img = cv2.imread(fileName,0)
tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"' 

txt = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)
print(txt)