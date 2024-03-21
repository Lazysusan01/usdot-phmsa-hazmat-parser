import os

def escape_xml_chars(text):
    """
    Escapes special XML characters in text.
    """
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&apos;"))

def consolidate_code_to_xml(base_path, output_file, file_extensions=None, ignore_dirs=None, ignore_files=None):
    """
    Consolidates code from a directory into a single XML file, excluding specified directories and files.
    
    :param base_path: The base directory to search for files.
    :param output_file: The output XML file where the consolidated code will be saved.
    :param file_extensions: A list of file extensions to include (e.g., ['.py', '.js']). If None, all files are included.
    :param ignore_dirs: A list of directory names to ignore (e.g., ['node_modules', '.git']).
    :param ignore_files: A list of file names to ignore (e.g., ['README.md']).
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        outfile.write('<codebase>\n')
        
        for root, dirs, files in os.walk(base_path):
            # Skip ignored directories
            if ignore_dirs:
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                
            for file in files:
                # Skip ignored files
                if ignore_files and file in ignore_files:
                    continue
                
                if file_extensions is None or os.path.splitext(file)[1] in file_extensions:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            file_content = infile.read()
                            file_content_escaped = escape_xml_chars(file_content)
                            
                            outfile.write(f'  <file path="{escape_xml_chars(file_path)}" name="{escape_xml_chars(file)}">\n')
                            outfile.write(f'    <content>{file_content_escaped}</content>\n')
                            outfile.write('  </file>\n')
                    except UnicodeDecodeError:
                        print(f"Skipping file due to encoding issue: {file_path}")
        
        outfile.write('</codebase>\n')
    print(f"Consolidated code written to {output_file}")

# Example usage
# C:\Users\nico_chemwatch\OneDrive - Ucorp Pty Ltd T A Chemwatch\Documents\Python\Transport of dangerous goods  - Cleanup\hazmat-parser\images
base_directory = "/users/nico_chemwatch/OneDrive - Ucorp Pty Ltd T A Chemwatch/documents/python/Transport of dangerous goods  - Cleanup/hazmat-parser"  # Change this to the path of your codebase
output_file_name = "consolidated_code.xml"  # The name of the output file
file_types_to_include = ['.py', '.html',]  # Change this list based on the types of files you want to include
directories_to_ignore = []  # Directories to ignore
files_to_ignore = ['README.md']  # Files to ignore

consolidate_code_to_xml(base_directory, output_file_name, file_types_to_include, directories_to_ignore, files_to_ignore)
