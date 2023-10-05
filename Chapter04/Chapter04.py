# Core Pkgs
import streamlit as st
st.set_page_config(page_title="NLP Web App", page_icon="👍", layout="centered", initial_sidebar_state="auto")

# NLP Pkgs
from textblob import TextBlob
import spacy
import neattext as nt

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


def main():
  """NLP web app with Streamlit"""

  title_template = """
  <div style="background-color:blue; padding:8px;">
  <h1 style="color:cyan">NLP Web App</h1>
  </div>
  """

  st.markdown(title_template, unsafe_allow_html=True)

  subheader_template = """
  <div style="background-color:cyan; padding:8px;">
  <h3 style="color:blue">Powered by Streamlit</h1>
  </div>
  """

  st.markdown(subheader_template, unsafe_allow_html=True)

  activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
  choice = st.sidebar.selectbox("Menu", activity)

  if choice == "Text Analysis":
    st.subheader("Text Analysis")
    st.write("")

  if choice == "Translation":
    st.subheader("Translation")
    st.write("")

  if choice == "Sentiment Analysis":
    st.subheader("Sentiment Analysis")
    st.write("")

  if choice == "About":
    st.subheader("About")
    st.write("")

    st.markdown("""
    ### NLP Web App made with Streamlit
    
    for info:
    - [streamlit](https://streamlit.io)
    """)


if __name__ == "__main__":
  main()