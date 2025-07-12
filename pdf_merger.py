import PyPDF2
import io
from typing import List, Union

class PDFMerger:
    """
    A class to handle PDF merging operations with proper error handling.
    """
    
    def __init__(self):
        """Initialize the PDF merger."""
        self.pdf_files = []
        self.merger = PyPDF2.PdfMerger()
    
    def add_pdf(self, file_obj: Union[io.BytesIO, io.BufferedReader]) -> None:
        """
        Add a PDF file to the merger.
        
        Args:
            file_obj: File object containing PDF data
            
        Raises:
            ValueError: If the file is not a valid PDF
            Exception: If there's an error reading the PDF
        """
        try:
            # Reset file pointer to beginning
            file_obj.seek(0)
            
            # Create a copy of the file data
            pdf_data = io.BytesIO(file_obj.read())
            
            # Validate that it's a valid PDF
            pdf_reader = PyPDF2.PdfReader(pdf_data)
            
            # Check if PDF has pages
            if len(pdf_reader.pages) == 0:
                raise ValueError("PDF file contains no pages")
            
            # Reset pointer for merger
            pdf_data.seek(0)
            
            # Add to merger
            self.merger.append(pdf_data)
            self.pdf_files.append(pdf_data)
            
        except PyPDF2.errors.PdfReadError as e:
            raise ValueError(f"Invalid PDF file: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")
    
    def merge(self) -> io.BytesIO:
        """
        Merge all added PDF files into a single PDF.
        
        Returns:
            io.BytesIO: Merged PDF as bytes
            
        Raises:
            ValueError: If no PDF files have been added
            Exception: If there's an error during merging
        """
        if not self.pdf_files:
            raise ValueError("No PDF files to merge")
        
        try:
            # Create output buffer
            output_buffer = io.BytesIO()
            
            # Write merged PDF to buffer
            self.merger.write(output_buffer)
            
            # Reset buffer pointer
            output_buffer.seek(0)
            
            return output_buffer
            
        except Exception as e:
            raise Exception(f"Error merging PDFs: {str(e)}")
    
    def get_file_count(self) -> int:
        """
        Get the number of PDF files added to the merger.
        
        Returns:
            int: Number of PDF files
        """
        return len(self.pdf_files)
    
    def clear(self) -> None:
        """
        Clear all added PDF files and reset the merger.
        """
        self.pdf_files.clear()
        self.merger.close()
        self.merger = PyPDF2.PdfMerger()
    
    def get_total_pages(self) -> int:
        """
        Get the total number of pages across all added PDF files.
        
        Returns:
            int: Total number of pages
        """
        total_pages = 0
        for pdf_file in self.pdf_files:
            try:
                pdf_file.seek(0)
                reader = PyPDF2.PdfReader(pdf_file)
                total_pages += len(reader.pages)
            except Exception:
                continue
        return total_pages
    
    def validate_pdf_file(self, file_obj: Union[io.BytesIO, io.BufferedReader]) -> dict:
        """
        Validate and get information about a PDF file.
        
        Args:
            file_obj: File object containing PDF data
            
        Returns:
            dict: Information about the PDF file
            
        Raises:
            ValueError: If the file is not a valid PDF
        """
        try:
            file_obj.seek(0)
            pdf_reader = PyPDF2.PdfReader(file_obj)
            
            info = {
                'is_valid': True,
                'pages': len(pdf_reader.pages),
                'encrypted': pdf_reader.is_encrypted,
                'metadata': pdf_reader.metadata if pdf_reader.metadata else {}
            }
            
            # Reset file pointer
            file_obj.seek(0)
            
            return info
            
        except PyPDF2.errors.PdfReadError as e:
            raise ValueError(f"Invalid PDF file: {str(e)}")
        except Exception as e:
            raise Exception(f"Error validating PDF: {str(e)}")
    
    def __del__(self):
        """Cleanup when the object is destroyed."""
        try:
            self.merger.close()
        except:
            pass
