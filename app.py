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
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)
import streamlit as st
import os
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)
import streamlit as st
import os
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)
import streamlit as st
import os
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)
import streamlit as st
import os
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)
import streamlit as st
import os
from PIL import Image

# Create a folder to save the captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Define a callback function for when the camera input changes
def on_camera_change(image_data, *args, **kwargs):
    # Display the captured image
    st.image(image_data, caption='Captured Image', use_column_width=True)

    # Save the captured image to a folder
    image = Image.open(image_data)
    image_path = os.path.join("captured_images", "captured_image.png")
    image.save(image_path)
    st.success(f"Image saved successfully at {image_path}")

# Create a camera input widget
st.title("Capture Image with Streamlit")
st.write("Click the button to capture an image from your camera.")
st.camera_input(
    label="Capture Image",
    key="camera_input",
    on_change=on_camera_change,
    label_visibility="visible"
)


