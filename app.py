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







import streamlit as st
st.write("Installing OpenCV...")
st.system("pip install opencv-python-headless")
import cv2
import os
from github import Github

# Function to take a photo using webcam
def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Function to upload image to GitHub
def upload_to_github(image_path, image_name):
    github_token = st.secrets["github_token"]  # Store your GitHub token securely in Streamlit Secrets
    repo_name = "pritipaul/DementiaImage_input"  # Change this to your GitHub repository name
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    with open(image_path, 'rb') as file:
        content = file.read()
    repo.create_file(f"images/{image_name}.jpg", "Uploaded photo", content)

def main():
    st.title("Webcam Photo Uploader")

    if st.button("Take Photo"):
        photo = take_photo()
        image_name = st.text_input("Enter photo name:")
        if image_name:
            image_path = f"{image_name}.jpg"
            cv2.imwrite(image_path, photo)
            st.image(photo, caption='Captured Photo', use_column_width=True)

            # Upload photo to GitHub
            upload_to_github(image_path, image_name)
            st.success("Photo uploaded to GitHub!")
        else:
            st.warning("Please enter a valid photo name.")

if __name__ == "__main__":
    main()
