# Core Pkgs
import streamlit as st
st.set_page_config(page_title="Covid19 Detection Tool", page_icon="covid19.jpeg", layout='centered', initial_sidebar_state='auto')

import os
import time

# Viz Pkgs
import cv2
from PIL import Image,ImageEnhance
import numpy as np 

# AI Pkgs
import tensorflow as tf


def main():
	"""Simple Tool for Covid-19 Detection from Chest X-Ray"""
	html_templ = """
	<div style="background-color:blue;padding:10px;">
	<h1 style="color:yellow">Covid-19 Detection Tool</h1>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)
	st.write("A simple proposal for Covid-19 Diagnosis powered by Deep Learning and Streamlit")

	st.sidebar.image("covid19.jpeg",width=300)

	image_file = st.sidebar.file_uploader("Upload an X-Ray Image (jpg, png or jpeg)",type=['jpg','png','jpeg'])

	if image_file is not None:
		our_image = Image.open(image_file)

		if st.sidebar.button("Image Preview"):
			st.sidebar.image(our_image,width=300)

		activities = ["Image Enhancement","Diagnosis", "Disclaimer and Info"]
		choice = st.sidebar.selectbox("Select Activty",activities)

		if choice == 'Image Enhancement':
			st.subheader("Image Enhancement")

			enhance_type = st.sidebar.radio("Enhance Type", ["Original", "Contrast", "Brightness"])

			if enhance_type == "Contrast":
				c_rate = st.slider("Contrast", 0.5, 5.0)
				enhancer = ImageEnhance.Contrast(our_image)
				img_output = enhancer.enhance(c_rate)
				st.image(img_output, width=600, use_column_width=True)

			elif enhance_type == "Brightness":
				c_rate = st.slider("Brightness", 0.5, 5.0)
				enhancer = ImageEnhance.Brightness(our_image)
				img_output = enhancer.enhance(c_rate)
				st.image(img_output, width=600, use_column_width=True)				

			else:
				st.text("Original Image")
				st.image(our_image, width=600, use_column_width=True)	


		elif choice == 'Diagnosis':
			pass

		else:
			st.subheader("Disclaimer and Info")
			st.subheader("Disclaimer")
			st.write("**This Tool is just a DEMO about Artificial Neural Networks so there is no clinical value in its diagnosis and the author is not a Doctor!**")
			st.write("**Please don't take the diagnosis outcome seriously and NEVER consider it valid!!!**")
			st.subheader("Info")
			st.write("This Tool gets inspiration from the following works:")
			st.write("- [Detecting COVID-19 in X-ray images with Keras, TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/)") 
			st.write("- [Fighting Corona Virus with Artificial Intelligence & Deep Learning](https://www.youtube.com/watch?v=_bDHOwASVS4)") 
			st.write("- [Deep Learning per la Diagnosi del COVID-19](https://www.youtube.com/watch?v=dpa8TFg1H_U&t=114s)")
			st.write("We used 206 Posterior-Anterior (PA) X-Ray [images](https://github.com/ieee8023/covid-chestxray-dataset/blob/master/metadata.csv) of patients infected by Covid-19 and 206 Posterior-Anterior X-Ray [images](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) of healthy people to train a Convolutional Neural Network (made by about 5 million trainable parameters) in order to make a classification of pictures referring to infected and not-infected people.")
			st.write("Since dataset was quite small, some data augmentation techniques have been applied (rotation and brightness range). The result was quite good since we got 94.5% accuracy on the training set and 89.3% accuracy on the test set. Afterwards the model was tested using a new dataset of patients infected by pneumonia and in this case the performance was very good, only 2 cases in 206 were wrongly recognized. Last test was performed with 8 SARS X-Ray PA files, all these images have been classified as Covid-19.")
			st.write("Unfortunately in our test we got 5 cases of 'False Negative', patients classified as healthy that actually are infected by Covid-19. It's very easy to understand that these cases can be a huge issue.")
			st.write("The model is suffering of some limitations:")
			st.write("- small dataset (a bigger dataset for sure will help in improving performance)")
			st.write("- images coming only from the PA position")
			st.write("- a fine tuning activity is strongly suggested")
			st.write("")
			st.write("Anybody has interest in this project can drop me an email and I'll be very happy to reply and help.")



	if st.sidebar.button("About the Author"):
		st.sidebar.subheader("Covid-19 Detection Tool")
		st.sidebar.markdown("by [Author's Name](https://www.authorswebsite.com)")
		st.sidebar.markdown("[author@gmail.com](mailto:author@gmail.com)")
		st.sidebar.text("All Rights Reserved (2023)")


if __name__ == '__main__':
		main()	