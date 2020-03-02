import cv2
import pytesseract
import os
from PIL import Image
import sys
import numpy as np
def get_string(img):
    cv2.imwrite("thres.png",img)
    result = pytesseract.image_to_string(Image.open("thres.png"))
    os.remove("thres.png")

    return result
