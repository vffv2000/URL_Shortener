from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from db.managers.url_manager import URLManager
from db.session import get_db
from services.url_service import URLService
redirect_router = APIRouter()


@redirect_router.get("/s/{code}")
def redirect(code: str, db: Session = Depends(get_db)):
    service = URLService(URLManager(db))
    url = service.get_redirect_url(code)
    return RedirectResponse(url=url, status_code=307)