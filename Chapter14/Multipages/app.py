import streamlit as st

my_variable = "From Main app.py Page"

def main():
	st.title("Streamlit Multi-page")
	st.subheader("Main Page")
	st.write(my_variable)



if __name__ == '__main__':
	main()

