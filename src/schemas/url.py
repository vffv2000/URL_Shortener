from datetime import datetime
from pydantic import BaseModel, HttpUrl


class ShortenIn(BaseModel):
    url: HttpUrl  # Валидирует формат (http/https), при ошибке FastAPI вернет 422


class ShortenOut(BaseModel):
    code: str
    short_url: str


class StatsOut(BaseModel):
    code: str
    original_url: str
    clicks: int
    created_at: datetime