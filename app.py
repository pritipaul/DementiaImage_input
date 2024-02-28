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

def save_uploaded_file(uploaded_file, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Saved file: {folder_path}/{uploaded_file.name}")

def main():
    st.title("Image Uploader and Saver")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        folder_path = "uploaded_images"
        if st.button("Save Image"):
            save_uploaded_file(uploaded_file, folder_path)

if __name__ == "__main__":
    main()
