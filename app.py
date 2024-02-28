import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

# Button to save the image
if st.button('Save Image'):
    if picture:
        picture.save("image")  # Change the path as needed
        st.success("Image saved successfully!")
    else:
        st.warning("No image to save!")
