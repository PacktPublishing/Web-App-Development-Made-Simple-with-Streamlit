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

		elif choice == 'Diagnosis':
			pass

		else:
			st.subheader("Disclaimer and Info")



	if st.sidebar.button("About the Author"):
		st.sidebar.subheader("Covid-19 Detection Tool")
		st.sidebar.markdown("by [Author's Name](https://www.authorswebsite.com)")
		st.sidebar.markdown("[author@gmail.com](mailto:author@gmail.com)")
		st.sidebar.text("All Rights Reserved (2023)")


if __name__ == '__main__':
		main()	