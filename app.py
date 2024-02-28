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

import core.ApiInformationLoadImage as info
import core.Introduction as intro
import streamlit as st
from PIL import Image
import CheckboxAdvanceExamples as advance
import StCheckboxBasicExamples as basic

image = Image.open('logo.jfif')
st.set_page_config(page_title='Learn Streamlit Widgets', page_icon=image, layout='wide', initial_sidebar_state='auto')


hide_streamlit_style = """
                <style>
                .css-k0sv6k { height: 1.875rem }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                .css-1l40rdr { text-align: left;}
                .css-sc0g0 { text-align: center;}
                #h1 { color: #431c5d }
                #h1 { color: #bccbde }
                #h1 { color: #cdd422 }
                #h1 { color: #3fb0ac }
                h1 { color: #431c5d }
                h2 { color: #431c5d }
                h3 { color: #3fb0ac }
                .css-145kmo2 { color: #3fb0ac }
                .css-h9oeas { color: #431c5d }
                .css-hi6a2p { max-width: 60% }
              //   .row_heading.level0 {display:none} 
                 tbody th {display:none}
                 .blank {display:none}
                 .css-y37zgl {text-align: left}
                 .css-hxt7ib { padding-top: 1rem}
                 .css-18e3th9 { padding-top: 3rem}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title('Streamlit Checkbox Live Coding', 'checkbox-radio')

with st.sidebar:
    st.markdown("<a href='https://www.youtube.com/channel/UCumeOi-LeRBGhVdzjXyAy1A'>Youtube: Python Techie</a>", unsafe_allow_html=True)
    colSA, colSB, colSC = st.columns([1,4,1])
    with colSA:
        st.write("")
    with colSB:
        st.image(image, width=100)
    with colSC:
        st.write("")
    st.title("Streamlit Checkbox")

    pages = {'ST.CHECKBOX API Ref': info,
             'ST.CHECKBOX Use Cases': intro,
             'Checkbox Basic Examples': basic,
             'Checkbox Advance Examples': advance,
             }
    page = st.sidebar.radio("", tuple(pages.keys()))
    colSX, colSY = st.columns([1, 1])
    with colSX:
        st.write("")
    colSK, colSZ = st.columns([1, 1])
    with colSK:
        st.write("")
    colSX, colSY = st.columns([1, 1])
    with colSX:
        st.write("")
    colSK, colSZ = st.columns([1, 1])
    with colSK:
        st.write("")
    colSX, colSY = st.columns([1, 1])
    with colSX:
        st.write("")
    colSK, colSZ = st.columns([1, 1])
    with colSK:
        st.write("")
    colSX, colSY = st.columns([1, 1])
    with colSX:
        st.write("")

    st.video('https://www.youtube.com/watch?v=hLGUvZAtQNE&t=74s')
    st.video('https://www.youtube.com/watch?v=NgR5u6w4MRg')
if page == 'ST.CHECKBOX API Ref':
    info.st_api_information()
elif page == 'ST.CHECKBOX Use Cases':
    intro.st_introduction()
elif page == 'Checkbox Basic Examples':
    basic.checkbox_basic_examples()
elif page == 'Checkbox Advance Examples':
    advance.checkbox_advance_examples()
