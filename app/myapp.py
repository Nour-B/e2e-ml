import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Location Image Classifier")
st.text("Provide URL of Location Image for image classification")

@st.cache_resource
def load_model():
  model = tf.keras.models.load_model('./models/')
  return model

with st.spinner('Loading Model Into Memory....'):
  model = load_model()

classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)  
  img = tf.image.resize(img,[150,150])
  return np.expand_dims(img, axis=0)

# path = st.text_input('Enter Image URL to Classify.. ','https://storage.googleapis.com/image_classification_2021/Glacier-Argentina-South-America-blue-ice.JPEG')
# path = st.text_input('Enter Image URL to Classify.. ','https://drive.google.com/drive/folders/1uKVwdALZ8grM3SN06UnxuWxx4oRbVAAJ/alto-crew-Rv3ecImL4ak-unsplash.jpg')
# if path is not None:
    # content = requests.get(path).content
    # with open("./alto-crew-Rv3ecImL4ak-unsplash.jpg", "rb") as f:
    #  content = f.read()
uploaded_file = st.file_uploader("Choose a file", type=["png","jpg","jpeg","bmp","gif"])
if uploaded_file is not None:
  # To read file as bytes:
  content = uploaded_file.getvalue()

  st.write("Predicted Class :")
  with st.spinner('classifying.....'):
    label =np.argmax(model.predict(decode_img(content)),axis=1)
    st.write(classes[label[0]])    
  st.write("")
  image = Image.open(BytesIO(content))
  st.image(image, caption='Classifying Image', use_column_width=True)