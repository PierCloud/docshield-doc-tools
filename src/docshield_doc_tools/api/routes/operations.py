from fastapi import APIRouter

from docshield_doc_tools.services.operations import supported_operations

router = APIRouter()


@router.get("")
async def list_operations() -> dict[str, list[str]]:
    return {"operations": supported_operations()}

