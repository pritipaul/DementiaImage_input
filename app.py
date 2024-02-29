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
#             if not os.path.exists("DementiaImage_input/images/"):
#                 os.makedirs("DementiaImage_input/images/")

#             # Save the image
#             file_path = os.path.join("DementiaImage_input/images/", f"{image_name}.jpg")
#             image.save(file_path)
#             st.success(f"Image saved as '{image_name}.jpg' successfully!")
#         else:
#             st.warning("Please enter an image name!")













import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import cv2

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('/content/my_model2.hdf5')
    return model

with st.spinner('Model is being loaded..'):
    model = load_model()

st.write("""
         # Flower Classification
         """
         )

file = st.file_uploader("Please upload a brain scan file", type=["jpg", "png"])

st.set_option('deprecation.showfileUploaderEncoding', False)

def import_and_predict(image_data, model):
    size = (180, 180)    
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    # For binary classification, you only have one class, so you can directly use the prediction
    # as the confidence score.
    confidence_score = prediction[0][0]
    
    if confidence_score > 0.5:
        st.write("The model predicts that this is a positive class with {:.2f}% confidence.".format(confidence_score * 100))
    else:
        st.write("The model predicts that this is a negative class with {:.2f}% confidence.".format((1 - confidence_score) * 100))




