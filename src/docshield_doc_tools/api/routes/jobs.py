from fastapi import APIRouter, HTTPException, status

from docshield_doc_tools.models.job import JobRequest, JobResponse
from docshield_doc_tools.services.dispatcher import execute_job

router = APIRouter()


@router.post("", response_model=JobResponse, status_code=status.HTTP_202_ACCEPTED)
async def create_job(payload: JobRequest) -> JobResponse:
    try:
        return execute_job(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

