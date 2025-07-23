# PDF Insight Agent – AI-Powered PDF Summarizer

*Date of creation: 2025-07-23*

## Application description

PDF Insight AI is a modern web application (Streamlit) that allows you to quickly and easily extract the most important information and generate summaries from any PDF files—including contracts, offers, reports, or business correspondence.

The application uses the large language model Llama 3 70B (LLM) provided by the Groq platform, ensuring fast, accurate, and natural text processing—both in Polish and English.

**Key features:**

- **Extraction of key information:** The tool automatically lists the most important data from the document in clear bullet points.
- **Summary generation:** The AI creates a concise summary of the document (3–5 sentences) in Polish or English.
- **Clear PDF preview:** Quickly view the PDF text in the first tab.
- **Ease of use:** The application works in your browser, requires no installation, and does not store user files.
- **AI-powered analysis (Groq + Llama3-70B):** Fast and efficient analysis even for longer documents, supporting both Polish and English.

**How does it work?**

1. The user generates a free API key on the Groq platform and pastes it into the application.
2. After uploading a PDF file, the app extracts the text and sends a query to the AI model.
3. On a separate tab, the app displays in aesthetic boxes: Key Information (bullet points) and Summary (a short synthesis of the whole).
4. The user can instantly use the generated data—for example, in a report, email, or meeting summary.

**Example use cases:**

- Quickly understanding the content of offers, contracts, technical documentation, or official letters.
- Extracting key facts for reports, analyses, or summaries.
- Automatically generating summaries from files shared by coworkers.

## Skills

- **Python**
- **Streamlit**
- **PyPDF2**
- **Requests**
- **Pandas**
- **Groq API**
- **Llama 3 70B (LLM)**
- **UI/UX Design**

## Project structure

The project consists of several files and resources needed to run the PDF Insight AI application:

- **app.py** – Main Streamlit application file; handles PDF upload, extraction, and AI-powered summarization.
- **requirements.txt** – List of Python package dependencies required to run the app.
- **README.md** – Project documentation and usage instructions.
- **Api groq.png** – Helper image showing how to generate an API key on the Groq platform.

## Example Images from Application in Use

## Explore the app:

[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?logo=github)](https://github.com/jcwigon/pdf_summarization_aiagent)
&nbsp;
[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://pdfsummarizationaiagent-5u7fuvywmjy8wav5cudj8g.streamlit.app/)



