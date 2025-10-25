from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/shop_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    WAYFORPAY_MERCHANT: str = ""
    WAYFORPAY_SECRET: str = ""
    NP_API_KEY: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
