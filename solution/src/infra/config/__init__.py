from dotenv import load_dotenv
from src.infra.config.schemas import Settings

load_dotenv(override=True)
SETTINGS = Settings()
