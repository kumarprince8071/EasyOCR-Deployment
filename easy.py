import easyocr
from easyocr import *
from PIL import Image



def detect_text(image):
    reader = easyocr.Reader(["en","ar"])
    text = reader.readtext(image,detail=0,paragraph=True)
    return text
    '''for i in text:
        return i[1]'''

print(detect_text(r"C:\Users\kumar\Downloads\tes.jpg"))