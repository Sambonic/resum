from src.parser import summarize_pdf
from src.chatbot import send_prompt

# Put the path to the research
pdf_path = "pdf/research.pdf"
text = summarize_pdf(pdf_path)

if text:
  print(send_prompt(text))
else:
  print("No summaries could be generated")