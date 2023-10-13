import streamlit as st

st.set_page_config(
	page_title = "Hello World!",
	page_icon = "😃",
	layout = "centered", #wide
	initial_sidebar_state = "expanded", #collapsed, auto
	menu_items = {
		"Get Help": "https://streamlit.io",
		"Report a bug": "https://github.com",
		"About":  "About my application **Hello World!**"
	}
	)


st.sidebar.title("Hello World!")
st.title("Hello World!")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


