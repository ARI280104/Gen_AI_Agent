#Executing the GUI
import streamlit as st

def main():
    st.set_page_config(page_title="Gen AI", page_icon="books",)
    st.header("Chat with your Healthcare Documents")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your healthcare documents and click on process", type=["pdf", "docx", "txt"])
        st.button("Process")
        if __name__ == "__main__":
            main()