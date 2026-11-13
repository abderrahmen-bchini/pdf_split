# PDF Split

A simple terminal tool that splits a PDF into two files — one with the odd pages and one with the even pages — so you can print double-sided on a printer that only prints single-sided: print the odd-page file, flip the stack, then print the even-page file.

## Requirements

- Python 3
- [pypdf](https://pypi.org/project/pypdf/)

## Setup

```bash
# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirement.txt
```

## Usage

```bash
python pdf_split.py <file.pdf>
```

This creates a folder named `print_<file>` next to the original PDF, containing:

- `<file>_odd.pdf` — odd pages (1, 3, 5, ...)
- `<file>_even.pdf` — even pages (2, 4, 6, ...)

### Example

```bash
python pdf_split.py document.pdf
```

Produces:

```
document.pdf
print_document/
├── document_odd.pdf
└── document_even.pdf
```
