import streamlit as st
from PIL import Image

# Database Management
import sqlite3
conn = sqlite3.connect('userdata.db')
c = conn.cursor()

#Hashing Function (passlib,hashlib,bcrypt,scrypt)
import hashlib

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


# Data Base Functions
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_data(username,password):	
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()


def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data 


def main():
	"""Login & Signuo Skeleton"""

	html_temp = """
	<div style=background-color:{};padding:10px;border-radius:10px">
	<h1 style="color:{};text-align:center:">Login/Signup Skeleton</h1>
	</div>
	"""

	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)

	menu = ["Home", "Login", "SignUp", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Home":
		st.subheader("Login with Password Hashing and local DB Storage.")
		st.header("Home")

		st.image("login.png", use_column_width = True)

	elif choice == "Login":
		username = st.sidebar.text_input("Username")
		password = st.sidebar.text_input("Password",type='password')

		if st.sidebar.checkbox("Login"):
			st.subheader("NAME of YOUR APP Here!")
			create_table()

			hashed_pswd_init = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd_init))

			if result:
				st.success("Logged In as: {}".format(username))
				task = st.selectbox("Task",["Task A","Task B"])


			else:
				st.warning("Incorrect Username/Password")


	elif choice == "SignUp":
		st.subheader("Create An Account")
		new_username = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		if st.button("Sign Up"):
			create_table()

			hashed_pswd = make_hashes(new_password)
			add_data(new_username,hashed_pswd)

			st.success("You have successfully created an Account")

	else:
		st.subheader("About Section")


if __name__ == '__main__':
	main()	