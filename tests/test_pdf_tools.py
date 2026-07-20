from pathlib import Path

from pypdf import PdfReader
from reportlab.pdfgen import canvas

from docshield_doc_tools.services.pdf_tools import merge_pdfs


def make_pdf(path: Path, text: str) -> None:
    pdf = canvas.Canvas(str(path))
    pdf.drawString(72, 720, text)
    pdf.showPage()
    pdf.save()


def test_merge_pdfs(tmp_path: Path) -> None:
    first = tmp_path / "first.pdf"
    second = tmp_path / "second.pdf"
    output = tmp_path / "merged.pdf"
    make_pdf(first, "first")
    make_pdf(second, "second")

    result = merge_pdfs([first, second], output)

    assert result == output
    reader = PdfReader(str(output))
    assert len(reader.pages) == 2

