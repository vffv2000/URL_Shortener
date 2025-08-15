from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from db.managers.url_manager import URLManager
from db.session import get_db
from schemas.url import ShortenOut, ShortenIn, StatsOut
from services.url_service import URLService

v1_url_router = APIRouter()


@v1_url_router.post("/shorten", response_model=ShortenOut, status_code=201)
def shorten_url(payload: ShortenIn, request: Request, db: Session = Depends(get_db)):
    """
    Endpoint to shorten a given URL.

    Args:
        payload (ShortenIn): Input payload containing the original URL.
        request (Request): FastAPI request object to build the shortened URL.
        db (Session, optional): Database session provided by dependency injection.

    Returns:
        ShortenOut: Object containing the shortened URL and its code.
    """
    service = URLService(URLManager(db))
    code = service.shorten_url(str(payload.url))
    short = str(request.base_url).rstrip("/") + f"/s/{code}"
    return ShortenOut(code=code, short_url=short)


@v1_url_router.get("/stats/{code}", response_model=StatsOut)
def stats(code: str, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve statistics for a shortened URL.

    Args:
        code (str): Short code of the URL.
        db (Session, optional): Database session provided by dependency injection.

    Returns:
        StatsOut: Object containing URL code, original URL, click count, and creation timestamp.
    """
    service = URLService(URLManager(db))
    row = service.get_stats(code)
    return StatsOut(
        code=row.code,
        original_url=row.original_url,
        clicks=row.clicks,
        created_at=row.created_at
    )
