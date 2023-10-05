import streamlit as st

# TEXT
#Title
st.title("Streamlit Basics")

# #Header
# st.header("This is a header")

# #Subheader
# st.subheader("This is a subheader")

# #Text
# st.text("This is a simple text")

# #Write
# st.write("This is a write dimension")

# st.header("Markdown and HTML")

# #Markdown
# # Hyperlinks
# st.markdown("[Streamlit](https://www.streamlit.io)")

# st.markdown("https://www.streamlit.io")

# #HTML
# html_page = """
# <div style="background-color:blue;padding:50px">
# 	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
# </div>
# """

# st.markdown(html_page, unsafe_allow_html=True)

# st.success("Success!")
# st.info("Information")
# st.warning("This is a warning")
# st.error("This is an error!")

# st.header("Images, Video and Audio")

# #Image
# from PIL import Image
# img = Image.open("packt.jpeg")
# st.image(img, width=300, caption="Packt Logo")

# #Video
# video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

# #Video from an URL
# st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

# #Audio
# audio_file = open("sample.mp3","rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes)

st.header("Widgets")

# #Button
# if st.button("Play"):
# 	st.text("Hello World!")

# #Checkbox
# if st.checkbox("Checkbox"):
# 	st.text("Checkbox selected")

# #Radio Button
# radio_but = st.radio("Your Selection", ["A", "B"])
# if radio_but == "A":
# 	st.info("You selected A")
# else:
# 	st.info("You selected B")


# #Selectbox
# city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

# #Multiselect
# occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

# #TEXT Input
# name = st.text_input("Your Name", "Write something...")
# st.text(name)

# #NUMBER Input
# age = st.number_input("Input a number")

# #TEXT Area
# message = st.text_area("Your Message", "Write something...")

# #SLIDER
# select_val = st.slider("Select a Value", 1, 10)

# #BALLOONS
# if st.button("ballons"):
# 	st.balloons()

# st.header("Dataframes and Tables")

# import pandas as pd
# df = pd.read_csv("auto.csv")
# st.dataframe(df.head(10))

# st.table(df.head(10))


# #PLOTTINGS
# st.area_chart(df[["mpg","cylinders"]])
# st.bar_chart(df[["mpg",	"cylinders"]].head(20))
# st.line_chart(df[["mpg","cylinders"]].head(20))

# #SEABORN
# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, ax = plt.subplots()
# corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot = True)
# st.pyplot(fig)

#Date and Time
# st.header("Date & Time")

# import datetime

# today = st.date_input("Today is", datetime.datetime.now())


# import time 

# hour = st.time_input("The time is", datetime.time(12,30))


# #DISPLAY JSON CODE
# data = {"name":"John","surname":"Wick"}
# st.json(data)

# #Displaying CODE
# st.code("import pandas as pd")

# julia_code = """
# function doit(num::int)
# 	println(num)
# end
# """

# st.code(julia_code, language='julia')


# st.header("Progress Bar and Spinner")

# #Progress Bar
# import time

# my_bar = st.progress(0)
# for value in range(100):
# 	time.sleep(1)
# 	my_bar.progress(value+1)

#SPINNER
import time

with st.spinner("Please wait..."):
	time.sleep(10)
st.success("Done!")

















