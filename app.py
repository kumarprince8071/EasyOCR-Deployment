import streamlit as st
from PIL import Image
import easyocr as ocr
import numpy as np
# title
st.title("Text Extraction Model Deployment")

image = st.file_uploader(label="Enter Your Image", type=['png', 'jpg', 'jpeg'])

def load_model():
    reader = ocr.Reader(['en'])
    return reader

reader = load_model()
if image is not None:
    input_image = Image.open(image)
    st.image(input_image)
    result = reader.readtext(np.array(input_image),detail=0,paragraph=True)
    st.header("Extracted Text")
    st.write(result)
else:
    st.write("Upload an Image")
