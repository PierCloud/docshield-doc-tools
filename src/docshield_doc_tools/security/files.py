from pathlib import Path

from docshield_doc_tools.core.config import settings

PDF_SIGNATURE = b"%PDF-"


def validate_input_file(path: Path) -> None:
    if not path.exists():
        raise ValueError(f"Input file does not exist: {path.name}")
    if not path.is_file():
        raise ValueError(f"Input path is not a file: {path.name}")
    if path.stat().st_size <= 0:
        raise ValueError(f"Input file is empty: {path.name}")
    if path.stat().st_size > settings.max_file_size_bytes:
        raise ValueError(f"Input file exceeds size limit: {path.name}")


def validate_pdf_file(path: Path) -> None:
    validate_input_file(path)
    with path.open("rb") as file:
        signature = file.read(len(PDF_SIGNATURE))
    if signature != PDF_SIGNATURE:
        raise ValueError(f"Input file is not a valid PDF by signature: {path.name}")


def validate_output_path(path: Path) -> None:
    if path.exists() and path.is_dir():
        raise ValueError("Output path points to a directory.")
    path.parent.mkdir(parents=True, exist_ok=True)

