from fastapi import APIRouter

from docshield_doc_tools.api.routes import jobs, operations

api_router = APIRouter()
api_router.include_router(operations.router, prefix="/operations", tags=["operations"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])

