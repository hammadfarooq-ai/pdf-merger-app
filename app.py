import streamlit as st
import io
import base64
from pdf_merger import PDFMerger
import os

# Configure the page
st.set_page_config(
    page_title="PDF Merger Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'file_names' not in st.session_state:
    st.session_state.file_names = []

def main():
    # Header
    st.title("📄 PDF Merger Pro")
    st.markdown("**Merge multiple PDF files into one document with ease!**")
    st.markdown("---")
    
    # Instructions
    with st.expander("ℹ️ How to use", expanded=False):
        st.markdown("""
        1. **Upload PDF files** using the file uploader below
        2. **Review the file list** and reorder if needed
        3. **Click 'Merge PDFs'** to combine all files in sequence
        4. **Download** your merged PDF file
        
        **Note:** Files will be merged in the order they appear in the list.
        """)
    
    # File upload section
    st.subheader("📁 Upload PDF Files")
    
    # File uploader with drag and drop
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=['pdf'],
        accept_multiple_files=True,
        help="Drag and drop PDF files here or click to browse"
    )
    
    # Process uploaded files
    if uploaded_files:
        # Update session state with new files
        new_files = []
        new_names = []
        
        for file in uploaded_files:
            if file not in st.session_state.uploaded_files:
                new_files.append(file)
                new_names.append(file.name)
        
        # Add new files to session state
        st.session_state.uploaded_files.extend(new_files)
        st.session_state.file_names.extend(new_names)
    
    # Display uploaded files
    if st.session_state.uploaded_files:
        st.subheader("📋 Uploaded Files")
        
        # Create columns for better layout
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.info(f"**{len(st.session_state.uploaded_files)} file(s) ready for merging**")
        
        with col2:
            if st.button("🗑️ Clear All", type="secondary"):
                st.session_state.uploaded_files = []
                st.session_state.file_names = []
                st.rerun()
        
        # Display file list with options to remove individual files
        for i, (file, name) in enumerate(zip(st.session_state.uploaded_files, st.session_state.file_names)):
            col1, col2, col3 = st.columns([0.5, 3, 1])
            
            with col1:
                st.write(f"**{i+1}.**")
            
            with col2:
                # Get file size
                file_size = len(file.getvalue()) / 1024  # Size in KB
                if file_size < 1024:
                    size_str = f"{file_size:.1f} KB"
                else:
                    size_str = f"{file_size/1024:.1f} MB"
                
                st.write(f"📄 {name} ({size_str})")
            
            with col3:
                if st.button("❌", key=f"remove_{i}", help="Remove this file"):
                    st.session_state.uploaded_files.pop(i)
                    st.session_state.file_names.pop(i)
                    st.rerun()
        
        st.markdown("---")
        
        # Merge button and options
        if len(st.session_state.uploaded_files) >= 2:
            st.subheader("🔄 Merge Settings")
            
            # Output filename
            output_filename = st.text_input(
                "Output filename",
                value="merged_document.pdf",
                help="Enter the name for your merged PDF file"
            )
            
            # Ensure .pdf extension
            if not output_filename.endswith('.pdf'):
                output_filename += '.pdf'
            
            # Merge button
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col2:
                merge_button = st.button(
                    "🔀 Merge PDFs",
                    type="primary",
                    use_container_width=True
                )
            
            if merge_button:
                try:
                    # Show progress
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Initialize PDF merger
                    merger = PDFMerger()
                    
                    # Process each file
                    for i, file in enumerate(st.session_state.uploaded_files):
                        status_text.text(f"Processing file {i+1}/{len(st.session_state.uploaded_files)}: {st.session_state.file_names[i]}")
                        progress_bar.progress((i + 1) / len(st.session_state.uploaded_files))
                        
                        # Reset file pointer
                        file.seek(0)
                        
                        # Add file to merger
                        merger.add_pdf(file)
                    
                    # Merge PDFs
                    status_text.text("Merging PDFs...")
                    merged_pdf = merger.merge()
                    
                    # Create download button
                    status_text.text("Preparing download...")
                    
                    # Encode PDF for download
                    b64_pdf = base64.b64encode(merged_pdf.getvalue()).decode()
                    href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="{output_filename}">Download {output_filename}</a>'
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    # Success message and download
                    st.success("✅ PDFs merged successfully!")
                    st.markdown(href, unsafe_allow_html=True)
                    
                    # Download button (alternative method)
                    st.download_button(
                        label="📥 Download Merged PDF",
                        data=merged_pdf.getvalue(),
                        file_name=output_filename,
                        mime="application/pdf",
                        type="primary"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error merging PDFs: {str(e)}")
                    st.error("Please make sure all uploaded files are valid PDF documents.")
        
        elif len(st.session_state.uploaded_files) == 1:
            st.warning("⚠️ Please upload at least 2 PDF files to merge.")
    
    else:
        # No files uploaded
        st.info("👆 Upload PDF files using the file uploader above to get started!")
        
        # Show some helpful tips
        st.markdown("### 💡 Tips:")
        st.markdown("""
        - You can upload multiple PDF files at once
        - Files will be merged in the order they appear
        - Supported file types: PDF only
        - Maximum file size depends on your system resources
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit and PyPDF2*")

if __name__ == "__main__":
    main()
