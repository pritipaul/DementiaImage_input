import streamlit as st

# Define a callback function for when the camera input changes
def on_camera_change(image_data):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

# Create a camera input widget
st.camera_input(
    label="Capture Image",
    key="camera_input",
    help="Click the button to capture an image from your camera.",
    on_change=on_camera_change,
    disabled=False,
    label_visibility="visible"
)
