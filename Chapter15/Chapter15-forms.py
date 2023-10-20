import streamlit as st

def main():
	st.title("Streamlit Forms Tutorial")


	# Method 1: with (Context Manager Approach)
	with st.form(key='form1'):
		firstname = st.text_input("Firstname")
		lastname = st.text_input("Lastname")
		complete_name = firstname + " " + lastname

		submit_button = st.form_submit_button(label="Register")

		if submit_button:
			st.success("Hello {} you have been regstered!".format(complete_name))

	# Method 2: no 'with' and submitting message outside
	form2 = st.form(key='form2')
	username = form2.text_input("Username")
	jobtype = form2.selectbox("Job", ["Streamlit Master", "NBA Player", "Sailorman"])
	submit_button2 = form2.form_submit_button("Login")

	if submit_button2:
			st.success("Hello {} you logged in!".format(username))



if __name__ == '__main__':
	main()