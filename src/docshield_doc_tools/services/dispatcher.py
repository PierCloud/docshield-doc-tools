from pathlib import Path

from docshield_doc_tools.core.config import settings
from docshield_doc_tools.models.job import JobRequest, JobResponse, JobStatus
from docshield_doc_tools.services.operations import supported_operations
from docshield_doc_tools.services.pdf_tools import merge_pdfs


def execute_job(payload: JobRequest) -> JobResponse:
    if payload.operation not in supported_operations():
        raise ValueError(f"Unsupported operation: {payload.operation}")
    if len(payload.input_refs) > settings.max_input_files:
        raise ValueError("Too many input files.")

    if payload.operation == "merge-pdf":
        output_ref = payload.options.get("output_ref")
        if not output_ref:
            raise ValueError("merge-pdf requires options.output_ref.")

        output_path = merge_pdfs(
            input_paths=[Path(ref) for ref in payload.input_refs],
            output_path=Path(output_ref),
        )
        return JobResponse(
            status=JobStatus.completed,
            operation=payload.operation,
            output_refs=[str(output_path)],
            message="PDF files merged successfully.",
        )

    raise ValueError(f"Unhandled operation: {payload.operation}")

