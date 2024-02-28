import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
import streamlit as st

# Display the image
if picture:
    st.image(picture)

# Input field for image name
image_name = st.text_input('Enter image name (without extension):')

# Button to save the image
if st.button('Save Image'):
    if picture:
        if image_name:
            file_path = f"path/to/your/image/{image_name}.jpg"  # Change the path as needed

            picture.save(file_path)
            st.success(f"Image saved as '{image_name}.jpg' successfully!")
        else:
            st.warning("Please enter an image name!")
    else:
        st.warning("No image to save!")


