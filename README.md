# URL Shortener API

A simple URL shortener service built with FastAPI and SQLAlchemy.

## Features

- Shorten long URLs to a unique code
- Redirect short URLs to the original URL
- Track click statistics for each short URL
- FastAPI-based API with automatic OpenAPI docs
- SQLite database (configurable via `settings.db_url`)

## Requirements

- Python >= 3.11
- Poetry (for dependency management)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd URL_Shortener
```
2. Install dependencies with Poetry:
```bash
poetry install
```
3. Run the application:

```bash
docker-compose up --build 
```
