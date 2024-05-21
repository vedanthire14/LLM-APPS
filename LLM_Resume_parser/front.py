import streamlit as st
from main import pipe
from pypdf import PdfReader


# Streamlit UI for uploading PDF
st.title("PDF Uploader and Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# If a file is uploaded
if uploaded_file is not None:
    # Display the filename
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Create a PDF reader object
    pdf_reader = PdfReader(uploaded_file)

    # Display the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    st.write(f"The PDF file contains {num_pages} pages.")

    # Display the content of each page
    st.write(f"Page content:")
    page = pdf_reader.pages[0]
    st.text(page.extract_text())
    content = page.extract_text()
    result = pipe.fit(content, domain="resume", labels=None)
    resume_content = result[0]['parsed']['data']['completion']
    # resume_content
    trial_data = {}

    for items in resume_content:
      key = items.get('T')
      value = items.get('E')

      if key in trial_data:
        if isinstance(trial_data[key],list):
          trial_data[key].append(value)
        else:
          trial_data[key] = [trial_data[key],value]
      else:
        trial_data[key] = value


    st.write(f"Page content:")
    st.text(trial_data)