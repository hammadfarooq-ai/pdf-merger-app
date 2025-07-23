# PDF Merger Pro

A simple and attractive web application for merging multiple PDF files into a single document. Built with Streamlit for an easy-to-use interface with drag-and-drop functionality.

![PDF Merger Pro](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Drag & Drop Upload**: Simply drag PDF files into the upload area
- **Sequential Merging**: Files are merged in the order you upload them
- **File Management**: Remove individual files or clear all at once
- **Progress Tracking**: Visual progress bar during merging process
- **Custom Output Names**: Choose your own filename for the merged PDF
- **File Information**: See file sizes and page counts before merging
- **Error Handling**: Clear error messages for invalid or corrupted PDFs

## How to Use

1. **Upload PDF Files**: Use the file uploader to select multiple PDF files
2. **Review File List**: Check the order and remove any unwanted files
3. **Set Output Name**: Enter a custom filename for your merged PDF
4. **Merge PDFs**: Click the merge button to combine all files
5. **Download**: Save your merged PDF to your computer

## Installation

### Requirements

- Python 3.11 or higher
- Streamlit
- PyPDF2

### Setup

1. Clone or download this project
2. Install the required packages:
   ```bash
   pip install streamlit PyPDF2
   ```
3. Run the application:
   ```bash
   streamlit run app.py --server.port 5000
   ```
4. Open your browser and go to `http://localhost:5000`

## Project Structure

```
├── app.py              # Main Streamlit application
├── pdf_merger.py       # PDF processing logic
├── .streamlit/
│   └── config.toml     # Streamlit configuration
├── README.md           # This file
└── requirements files  # Dependencies
```

## Technical Details

### Core Components

- **Frontend**: Streamlit web framework for the user interface
- **PDF Processing**: PyPDF2 library for PDF manipulation and merging
- **File Handling**: In-memory processing using BytesIO objects
- **State Management**: Streamlit session state for file persistence

### Key Features

- **Validation**: Checks for valid PDF format and readable files
- **Error Handling**: Comprehensive exception handling with user-friendly messages
- **Memory Efficient**: Processes files in memory without temporary file storage
- **Responsive Design**: Works well on desktop and mobile devices

## Supported File Types

- **Input**: PDF files only
- **Output**: Single merged PDF file
- **File Size**: Limited by available system memory

## Error Handling

The application handles common issues:
- Invalid or corrupted PDF files
- Empty PDF documents
- Memory limitations for very large files
- Network interruptions during upload

## Contributing

This is a simple project perfect for learning or customization. Feel free to:
- Add new features like reordering files
- Improve the user interface
- Add support for password-protected PDFs
- Optimize for larger file handling

## License

This project is open source and available under the MIT License.

## Built With

- [Streamlit](https://streamlit.io/) - Web framework for Python
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF manipulation library
- Python 3.11+ - Programming language

---

**Note**: This application processes files locally in your browser session. No files are stored on external servers, ensuring your document privacy and security.