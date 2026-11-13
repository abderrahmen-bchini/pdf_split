import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def extract_pages(reader, page_indexes, output_path):
    writer = PdfWriter()

    for page_index in page_indexes:
        writer.add_page(reader.pages[page_index])

    with output_path.open("wb") as output_file:
        writer.write(output_file)


def main():
    parser = argparse.ArgumentParser(
        description="Split a PDF into odd page and even page PDFs."
    )
    parser.add_argument("pdf", type=Path, help="Input PDF file")
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()

    if not pdf_path.is_file():
        parser.error(f"File not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        parser.error("Input file must have a .pdf extension")

    try:
        reader = PdfReader(str(pdf_path))

        if reader.is_encrypted:
            parser.error("PDF is encrypted. unlock it before splitting.")

        page_count = len(reader.pages)

        output_dir = pdf_path.with_name(f"print_{pdf_path.stem}")
        output_dir.mkdir(exist_ok=True)

        odd_path = output_dir / f"{pdf_path.stem}_odd.pdf"
        even_path = output_dir / f"{pdf_path.stem}_even.pdf"

        odd_indexes = range(0, page_count, 2)
        # even pages print back-to-front: after printing the odds and
        # flipping the stack, sheet order is reversed, so the last even
        # page must come first in the file and page 2 must come last.
        even_indexes = reversed(range(1, page_count, 2))

        extract_pages(reader, odd_indexes, odd_path)
        extract_pages(reader, even_indexes, even_path)

        print(f"PDF:   {pdf_path.name} ({page_count} pages)")
        print(f"Output folder: {output_dir}")
        print(f"Odd:   {odd_path.name} ({(page_count + 1) // 2} pages)")
        print(f"Even:  {even_path.name} ({page_count // 2} pages)")

    except Exception as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    main()

