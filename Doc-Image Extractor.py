import os
import re
from docx import Document

# Paths
docx_file = r"D:\python Extrator\Extra POC from Word\MLAP POCs 1 1.docx"
output_base_folder = r'path\POC'
os.makedirs(output_base_folder, exist_ok=True)

# Load document
doc = Document(docx_file)

# Function to make heading a valid folder name
def sanitize_folder_name(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name.strip())

# Function to extract images from runs
def extract_images(run, folder, counter):
    drawing_elements = run.element.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/picture}pic')
    for pic in drawing_elements:
        blip = pic.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
        if blip is not None:
            rId = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            image_part = doc.part.related_parts[rId]
            image_ext = image_part.content_type.split('/')[-1]
            image_name = f'image_{counter[0]}.{image_ext}'
            image_path = os.path.join(folder, image_name)
            with open(image_path, 'wb') as f:
                f.write(image_part.blob)
            counter[0] += 1

current_heading = None
counter = [1]  # mutable counter

for para in doc.paragraphs:
    if para.style.name.startswith('Heading'):
        current_heading = sanitize_folder_name(para.text)
        if current_heading:
            heading_folder = os.path.join(output_base_folder, current_heading)
            os.makedirs(heading_folder, exist_ok=True)
            counter[0] = 1
    if current_heading:
        for run in para.runs:
            extract_images(run, heading_folder, counter)

print("Images extracted successfully under folders named after headings.")
