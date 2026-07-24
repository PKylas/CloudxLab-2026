#! /usr/bin/python

import os
from openai import OpenAI
import pypdf


with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

def extract_pdf_text(pdf_path: str) -> str:
    """Extracts all text from a local PDF file."""
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        # Extract text and append a separator
        text += page.extract_text() + "\n"
    return text

# Example Usage
pdf_content = extract_pdf_text("financial_report.pdf")

# Inject directly into your agent's execution context
agent_prompt = f"Use this document context to answer the user query:\n\n{pdf_content}"