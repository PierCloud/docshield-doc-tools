from fastapi import FastAPI

from docshield_doc_tools.api.router import api_router
from docshield_doc_tools.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Document manipulation microservice for DocShield.",
    )
    app.include_router(api_router)

    @app.get("/health", tags=["system"])
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "docshield-doc-tools"}

    return app


app = create_app()

