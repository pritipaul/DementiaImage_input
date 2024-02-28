# import streamlit as st
# from PIL import Image
# import os

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

        #     # Save the image
        #     file_path = "image/{image_name}.jpg"  # Change the path as needed
        #     image.save(file_path)
        #     st.success(f"Image saved as '{image_name}.jpg' successfully!")
        # else:
        #     st.warning("Please enter an image name!")




import streamlit as st
from PIL import Image
import os

# Take a picture
picture = st.camera_input("Take a picture")
if picture:
    # Display the image
    st.image(picture)

    # Input field for image name
    image_name = st.text_input('Enter image name (without extension):')

    # Button to save the image
    if st.button('Save Image'):
        if image_name:
            # Convert UploadedFile object to PIL Image
            image = Image.open(picture)
            
            # Create directory if it doesn't exist
            if not os.path.exists("images"):
                os.makedirs("images")

            # Save the image
            file_path = os.path.join("images", f"{image_name}.jpg")
            image.save(file_path)
            st.success(f"Image saved as '{image_name}.jpg' successfully!")
        else:
            st.warning("Please enter an image name!")
