from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    base_url: str

    model_config = SettingsConfigDict(
        env_file='.env.dev',
        env_file_encoding='utf-8'
    )