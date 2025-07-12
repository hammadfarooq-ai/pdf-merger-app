# PDF Merger Pro

## Overview

PDF Merger Pro is a web-based application built with Streamlit that allows users to merge multiple PDF files into a single document. The application provides a simple drag-and-drop interface for uploading PDF files and combining them in a specified order.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web framework
- **Interface**: Single-page application with drag-and-drop file upload
- **State Management**: Streamlit session state for maintaining uploaded files and file names
- **Layout**: Wide layout with collapsible sidebar

### Backend Architecture
- **Core Logic**: Python-based PDF processing using PyPDF2 library
- **File Handling**: In-memory file processing using io.BytesIO objects
- **Error Handling**: Comprehensive exception handling for PDF validation and processing

## Key Components

### 1. Main Application (app.py)
- **Purpose**: Streamlit web interface and user interaction
- **Key Features**:
  - File upload with multiple PDF support
  - Interactive instructions panel
  - Session state management for file persistence
  - Responsive UI with custom page configuration

### 2. PDF Processing Engine (pdf_merger.py)
- **Purpose**: Core PDF merging functionality
- **Key Features**:
  - PDF validation and error handling
  - In-memory file processing for efficiency
  - PyPDF2 integration for PDF manipulation
  - Type hints for better code maintainability

### 3. Error Handling Strategy
- **Validation**: Checks for valid PDF format and non-empty documents
- **Exception Management**: Specific error types for different failure scenarios
- **User Feedback**: Clear error messages for troubleshooting

## Data Flow

1. **File Upload**: Users drag-and-drop or select PDF files through Streamlit interface
2. **File Storage**: Uploaded files stored in session state as BytesIO objects
3. **Processing**: PDFMerger class validates and processes each PDF file
4. **Merging**: PyPDF2.PdfMerger combines all valid PDFs in sequence
5. **Download**: Merged PDF made available for download through Streamlit

## External Dependencies

### Core Libraries
- **Streamlit**: Web framework for the user interface
- **PyPDF2**: PDF manipulation and merging functionality
- **io**: In-memory file handling
- **base64**: File encoding for download functionality
- **os**: Operating system interface utilities

### File Format Support
- **Input**: PDF files only
- **Output**: Single merged PDF file
- **Validation**: PDF format verification and page count checking

## Deployment Strategy

### Local Development
- **Runtime**: Python environment with required dependencies
- **Server**: Streamlit development server
- **Configuration**: Page settings optimized for wide layout

### Production Considerations
- **Scalability**: In-memory processing suitable for moderate file sizes
- **Security**: File validation prevents malicious PDF uploads
- **Performance**: Sequential processing model for file merging

### Key Architectural Decisions

1. **Streamlit Choice**: Selected for rapid prototyping and simple deployment
   - **Pros**: Built-in UI components, easy file handling, minimal setup
   - **Cons**: Limited customization compared to full web frameworks

2. **PyPDF2 Integration**: Chosen for PDF manipulation
   - **Pros**: Mature library, comprehensive PDF support, active maintenance
   - **Cons**: Memory usage for large files, limited advanced features

3. **In-Memory Processing**: Files processed entirely in memory
   - **Pros**: Fast processing, no temporary file management
   - **Cons**: Memory constraints for very large files

4. **Session State Management**: Streamlit session state for file persistence
   - **Pros**: Simple state management, automatic cleanup
   - **Cons**: Limited to single user session, no persistence across sessions