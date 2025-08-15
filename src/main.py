from fastapi import FastAPI

from db.session import init_db
from routers.redirect_routes import redirect_router
from routers.v1.url_routes import  v1_url_router

app = FastAPI(title="URL Shortener", version="1.0.0")


@app.on_event("startup")
def on_startup() -> None:
    init_db()

# Версионный API
app.include_router(v1_url_router, prefix="/api/v1", tags=["URL API v1"])

# Редирект без API версии
app.include_router(redirect_router, tags=["Redirect"])