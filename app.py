# import streamlit as st
# from PIL import Image

# # Take a picture
# picture = st.camera_input("Take a picture")
# if picture:
#     # Display the image
#     st.image(picture)

#     # Input field for image name
#     image_name = st.text_input('Enter image name (without extension):')

#     # Button to save the image
#     if st.button('Save Image'):
#         if image_name:
#             # Convert UploadedFile object to PIL Image
#             image = Image.open(picture)

#             # Save the image
#             file_path = f"/image/{image_name}.jpg"  # Change the path as needed
#             image.save(file_path)
#             st.success(f"Image saved as '{image_name}.jpg' successfully!")
#         else:
#             st.warning("Please enter an image name!")


import streamlit as st
from PIL import Image
import os

# Create a folder to save images if it doesn't exist
SAVE_FOLDER = "images"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Take a picture
picture = st.camera_input("Take a picture")
if picture:
    # Save the image to the folder
    image_path = os.path.join(SAVE_FOLDER, "captured_image.png")
    with open(image_path, "wb") as f:
        f.write(picture)
    
    # Display the saved image
    st.image(image_path)


