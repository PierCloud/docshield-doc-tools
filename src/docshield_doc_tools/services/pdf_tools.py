from pathlib import Path

from pypdf import PdfReader, PdfWriter

from docshield_doc_tools.security.files import validate_output_path, validate_pdf_file


def merge_pdfs(input_paths: list[Path], output_path: Path) -> Path:
    if len(input_paths) < 2:
        raise ValueError("merge-pdf requires at least two input files.")

    validate_output_path(output_path)

    writer = PdfWriter()
    for input_path in input_paths:
        validate_pdf_file(input_path)
        reader = PdfReader(str(input_path), strict=True)
        if reader.is_encrypted:
            raise ValueError(f"Encrypted PDFs are not supported yet: {input_path.name}")
        for page in reader.pages:
            writer.add_page(page)

    with output_path.open("wb") as output_file:
        writer.write(output_file)

    return output_path

