from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DocShield Doc Tools"
    app_env: str = "local"
    api_v1_prefix: str = "/api/v1"
    workspace_dir: Path = Path("storage/jobs")
    max_input_files: int = Field(default=20, ge=1, le=100)
    max_file_size_mb: int = Field(default=50, ge=1, le=500)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def max_file_size_bytes(self) -> int:
        return self.max_file_size_mb * 1024 * 1024


settings = Settings()

