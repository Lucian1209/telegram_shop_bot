from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str = ""
    REDIS_URL: str = ""
    WAYFORPAY_MERCHANT: str = ""
    WAYFORPAY_SECRET: str = ""
    NP_API_KEY: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
