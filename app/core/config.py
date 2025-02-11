from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    App settings
    """

    PROJECT_NAME: str = "fastapi-social-network"
    AWS_REGION: str = Field(default="")
    AWS_ACCESS_KEY_ID: str = Field(default="")
    AWS_SECRET_ACCESS_KEY: str = Field(default="")
    DYNAMODB_TABLE: str = Field(default="")

    model_config = SettingsConfigDict(
        env_file=".env",
    )


settings = Settings()
