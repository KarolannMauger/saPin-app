import os

class Settings:
    API_TITLE = "saPin LED API"
    API_VERSION = "1.0.0"
    API_PREFIX = "/api/v1"
    LED_DRIVER = os.getenv("LED_DRIVER", "mock") # "mock" in dev, "rpi_ws281x" on PI
    API_KEY = os.getenv("API_KEY", "") # empty in dev
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*") # "*" in dev, frontend URL in prod

settings = Settings()
