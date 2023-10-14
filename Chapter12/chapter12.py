import streamlit as st
import pdfplumber
import docx2txt


def main():
	menu = ["Dropfiles", "About"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Dropfiles":
		st.subheader("Drag and Drop Files")

		raw_text_file = st.file_uploader("Upload File", type=['txt', 'docx', 'pdf'])
		if raw_text_file is not None:
			file_details = {"Filename":raw_text_file.name, "FileType": raw_text_file.type,  "FileSize": raw_text_file.size}
			st.write(file_details)

		# Check file type
		if raw_text_file.type == "text/plain":
			try:
				raw_text = str(raw_text_file.read(), "utf-8")
				st.info("Text from TXT file")
			except:
		 		st.warning("TXT File Fetching Problem...")	
		elif raw_text_file.type == "application/pdf":
			try:
				pdf_file = pdfplumber.open(raw_text_file)
				p0 = pdf_file.pages[0]
				raw_text = p0.extract_text()
				st.info("Text from PDF file")
			except:
		 		st.warning("PDF File Fetching Problem...")
		else:
			try:
				raw_text = docx2txt.process(raw_text_file)
				st.info("Text from DOCX file")
			except:
				st.warning("DOCX File Fetching Problem...")

		
		# Print the file content
		st.write(raw_text)




		# file_selection = st.radio("Select the file type", ['TXT','DOCX', 'PDF'])

		# if file_selection == 'TXT':
		# 	raw_text_file = st.file_uploader("Upload File", type=['txt'])
		# 	if raw_text_file is not None:
		# 		try:
		# 			raw_text = str(raw_text_file.read(), "utf-8")
		# 			st.info("Text from TXT file")
		# 			st.write(raw_text)
		# 		except:
		# 			st.warning("TXT File Fetching Problem...")	

		# elif file_selection == 'DOCX':
		# 	raw_text_file = st.file_uploader("Upload File", type=['docx'])
		# 	if raw_text_file is not None:
		# 		pass

		# else:
		# 	raw_text_file = st.file_uploader("Upload File", type=['pdf'])
		# 	if raw_text_file is not None:
		# 		pass



	else:
		st.subheader("Advanced File Uploading")


if __name__ == '__main__':
	main()