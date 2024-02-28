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
            
#             # Create directory if it doesn't exist
#             if not os.path.exists("images"):
#                 os.makedirs("images")

#             # Save the image
#             file_path = os.path.join("images", f"{image_name}.jpg")
#             image.save(file_path)
#             st.success(f"Image saved as '{image_name}.jpg' successfully!")
#         else:
#             st.warning("Please enter an image name!")



from PIL import Image
import glob


images = glob.glob("/path/to/images/")
index= st.number_input('Index')

if st.button('Next'):
    index+=1


if st.button('Prev'):
    if index > 0
        index = index -1

image = Image.open(images[index])
st.image(image, use_column_width=True)
