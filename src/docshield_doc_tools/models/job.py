from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class JobStatus(StrEnum):
    completed = "completed"
    failed = "failed"


class JobRequest(BaseModel):
    operation: str = Field(..., examples=["merge-pdf"])
    input_refs: list[str] = Field(default_factory=list)
    options: dict[str, Any] = Field(default_factory=dict)


class JobResponse(BaseModel):
    job_id: UUID = Field(default_factory=uuid4)
    status: JobStatus
    operation: str
    output_refs: list[str] = Field(default_factory=list)
    message: str

