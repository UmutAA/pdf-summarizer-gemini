# PDF Summarizer with Gemini 2.5 Flash Lite

A Python script that reads the first page of a PDF, summarizes its content, and extracts key keywords using **Gemini 2.5 Flash Lite**.

## Features

- Extracts text from the first page of any PDF file.
- Summarizes the text in a few sentences.
- Provides a list of key keywords.
- Built with Python and Gemini 2.5 Flash Lite API.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/UmutAA/pdf-summarizer-gemini.git
cd pdf-summarizer-gemini
``` 

2. Download required packages

```bash
pip install -r requirements.txt
```

3. Create an .env file and add your API key 

```bash
GOOGLE_API_KEY = "API KEY HERE"
```

4. Run the script

```bash
python summarize.py
```

5. Enter your PDF file's path

```bash
"C:/Users/USERNAME/Documents/PDFs/example.pdf"
```