import streamlit as st

# # Define a callback function for when the camera input changes
# def on_camera_change(image_data, *args, **kwargs):
#     # Display the captured image
#     st.image(image_data, caption='Captured Image', use_column_width=True)

# # Create a camera input widget
# st.camera_input(
#     label="Capture Image",
#     key="camera_input",
#     help="Click the button to capture an image from your camera.",
#     on_change=on_camera_change,
#     disabled=False,
#     label_visibility="visible"
# )

import streamlit as st
import os
import cv2
from PIL import Image
import numpy as np

def save_uploaded_file(uploaded_file, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Saved file: {folder_path}/{uploaded_file.name}")

def main():
    st.title("Image Uploader and Saver from Webcam")

    cap = cv2.VideoCapture(0)

    if st.button("Capture Image"):
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        st.image(image, caption='Captured Image', use_column_width=True)
        save_image = st.button("Save Image")
        if save_image:
            save_uploaded_file(image, "captured_images")

    cap.release()

if __name__ == "__main__":
    main()
