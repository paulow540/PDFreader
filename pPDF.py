# Import the required dependency

from PyPDF2 import PdfReader

# Define path of the PDF file
# 

pdf_file_name = 'Resume.*'


def my_pdf():
    # 
    # Open the file in binary mode for reading
    with open(pdf_file_name, 'rb') as pdf_file:
        # Read the PDF file
        pdf_reader = PdfReader(pdf_file)
        # Get number of pages in the PDF file
        page_nums = len(pdf_reader.pages)

        # Iterate over each page number
        for page_num in range(0, page_nums):
            # Read the PDF page
            page = pdf_reader.pages[page_num]
            # Extract text from PDF page
            text = page.extract_text()

            # Print text
            return text 
