#Executing the GUI
import streamlit as st
from dotenv import load_dotenv #in order to enable the .env file
from PyPDF2 import PdfReader
def get_pdf_text(pdf_docs): #here it is going to contain the raw texts 
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()#appending the text from each page]
    return text
def main():
    load_dotenv()  # Load environment variables from .env file
    st.set_page_config(page_title="Gen AI", page_icon="books",)
    st.header("Chat with your Healthcare Documents")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader()
        st.file_uploader("Upload your healthcare documents and click on process", accept_multiple_files=True)
        st.button("Process")

        
        with st.spinner("Processing"):
            #get pdf text
            raw_text = get_pdf_text(pdf_docs)
        #get the text chunks

        #create vector store
        if __name__ == "__main__":
            main()


