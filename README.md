# 📄 DOCX Image Extractor by Headings

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

</p>

---

## 📖 Overview

**DOCX Image Extractor by Headings** is a lightweight Python automation tool that extracts all embedded images from Microsoft Word (`.docx`) documents and automatically organizes them into folders based on the document's heading hierarchy.

Instead of manually copying screenshots from lengthy reports, this tool creates a clean folder structure where each heading becomes a separate directory containing all associated images.

It is particularly useful for:

- 🔐 Penetration Testing Reports
- 📋 Security Audit Documentation
- 📚 Technical Documentation
- 📝 User Manuals
- 📑 Compliance Reports
- 📂 Evidence Collection
- 🖼 Digital Asset Organization

---

# ✨ Features

- 📄 Reads Microsoft Word (.docx) files
- 🖼 Extracts every embedded image
- 📁 Automatically creates folders from document headings
- 🔒 Sanitizes invalid Windows/Linux filename characters
- ⚡ Fast and lightweight
- 💻 Cross-platform support
- 📦 Simple codebase
- 🚀 Easy to customize
- 🔄 Automatic image numbering
- 📂 Clean output structure

---

# 📸 Example

## Input Word Document

```
Heading 1
    Image
    Image

Heading 2
    Image

Heading 3
    Image
    Image
    Image
```

---

## Output

```
Output/

├── Heading 1/
│   ├── image_1.png
│   └── image_2.png
│
├── Heading 2/
│   └── image_1.jpg
│
└── Heading 3/
    ├── image_1.png
    ├── image_2.png
    └── image_3.png
```

---

# 🛠 Built With

- Python 3.9+
- python-docx
- os
- re

---

# 📂 Project Structure

```
docx-image-extractor/
│
├── extractor.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── sample/
│   └── sample_report.docx
│
├── output/
│
└── screenshots/
    ├── input.png
    └── output.png
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/docx-image-extractor.git
```

Move into the project directory

```bash
cd docx-image-extractor
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```
Python >= 3.9
python-docx
```

Install manually

```bash
pip install python-docx
```

---

# ▶ Usage

Open the script and edit the following paths:

```python
docx_file = r"sample/report.docx"

output_base_folder = r"output"
```

Run

```bash
python extractor.py
```

---

# 📂 Output Structure

```
output/

Authentication/

Business Logic/

SQL Injection/

IDOR/

XSS/
```

Each folder contains images extracted from that heading.

Example

```
SQL Injection/

image_1.png

image_2.png

image_3.png
```

---

# ⚙ How It Works

1. Loads the Word document.
2. Reads every paragraph.
3. Detects heading styles.
4. Creates a folder for each heading.
5. Searches for embedded images.
6. Extracts image binary data.
7. Saves images sequentially.
8. Continues until the document ends.

---

# 🚀 Use Cases

### Security

- Penetration Testing Reports
- Security Assessment Reports
- Vulnerability Documentation
- Compliance Evidence

### Documentation

- Software Manuals
- API Documentation
- User Guides
- Technical Specifications

### Education

- Lecture Notes
- Research Papers
- Laboratory Reports

### Business

- Audit Reports
- Internal Documentation
- Process Documents

---

# 🔒 Supported Formats

| Format | Supported |
|----------|-----------|
| PNG | ✅ |
| JPG | ✅ |
| JPEG | ✅ |
| GIF | ✅ |
| BMP | ✅ |
| TIFF | ✅ |

---

# 🧠 Algorithm

```
Load DOCX

↓

Read Paragraph

↓

Is Heading?

↓

Create Folder

↓

Search Images

↓

Extract Image

↓

Save Image

↓

Next Paragraph
```

---

# 📈 Performance

- Supports documents with hundreds of pages.
- Extracts thousands of images.
- Memory efficient.
- Lightweight processing.
- Fast execution.

---

# 🖥 Compatibility

| Operating System | Support |
|------------------|----------|
| Windows | ✅ |
| Linux | ✅ |
| macOS | ✅ |

---

# 📷 Screenshots

## Input

```
Word Document
```

(Add screenshot here)

---

## Output

```
Output Folder
```

(Add screenshot here)

---

# 🛣 Roadmap

- [ ] GUI Version (Tkinter)
- [ ] Drag & Drop Support
- [ ] Batch Processing
- [ ] Progress Bar
- [ ] ZIP Export
- [ ] PDF Support
- [ ] OCR Integration
- [ ] Logging
- [ ] Command Line Arguments
- [ ] Configuration File
- [ ] Recursive Folder Processing

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```
git checkout -b feature/NewFeature
```

3. Commit your changes

```
git commit -m "Added new feature"
```

4. Push

```
git push origin feature/NewFeature
```

5. Create a Pull Request

---

# 📝 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it.

---

# 🙌 Acknowledgements

- Python Community
- python-docx Developers
- Open Source Contributors

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it

---

# 📬 Contact

GitHub: **https://github.com/yourusername**

Email: **your.email@example.com**

---

# 🏷 Topics

```
python
python-docx
docx
word
office
automation
image-extractor
report
documentation
security
pentesting
audit
productivity
```

---

# 💡 Why Use This Project?

Manually extracting images from Word documents can be time-consuming and error-prone, especially for large reports with numerous screenshots. This tool automates the process by organizing images according to document headings, making it ideal for security assessments, audit reporting, technical documentation, and evidence management. It significantly improves productivity while maintaining a clean and structured output.
