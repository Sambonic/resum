from src.common_imports import *
from src.chatbot import send_prompt

def summarize_pdf(pdf_path: str) -> str:
  """
  This function opens the PDF and extracts text content.

  Args:
      pdf_path: Path to the PDF file.

  Returns:
      A string containing the extracted text from the PDF.
  """
  with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
      page = reader.pages[page_num]
      text += page.extract_text()
  return text