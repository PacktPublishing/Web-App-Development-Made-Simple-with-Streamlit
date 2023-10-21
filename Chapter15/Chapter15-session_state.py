import streamlit as st

def main():
	st.title("Streamlit Session State Tutorial")

	st.subheader("Counter Example")

	# Streamlit runs from top to bottom on every iteration so
	# we check if 'count' has already been initialized in st.session_state
	# if no, the initialize count to 0
	# if count is already initialized, don't do anything

	if 'count' not in st.session_state:
		st.session_state.count = 0



	# Create a button which will increment the counter
	increment = st.button('Increment')
	if increment:
		st.session_state.count += 1

	# A button to decrement the counter
	decrement = st.button('Decrement')
	if decrement:
		st.session_state.count -= 1	

	st.write("Count =", st.session_state.count )


	st.subheader("Callback Example - Mirrored Widgets")

	def update_first():
		st.session_state.second = st.session_state.first

	def update_second():
		st.session_state.first = st.session_state.second


	st.text_input(label="Textbox 1", key="first", on_change=update_first)
	st.text_input(label="Textbox 2", key="second", on_change=update_second)





if __name__ == '__main__':
	main()
