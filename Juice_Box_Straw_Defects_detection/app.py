import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

model = YOLO("best.pt")

st.title("Juice Box Straw Defect Detector")
st.write("Upload an image to detect defects")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img = np.array(image)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    results = model.predict(img_bgr, verbose=False)

    for result in results:
        predicted_class = model.names[result.probs.top1]
        confidence = result.probs.top1conf.item()

        st.success(f"Prediction: **{predicted_class}**")
        st.info(f"Confidence: **{confidence:.2%}**")

    st.image(image, caption="Uploaded Image", use_column_width=True)