FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Установка Poetry
ENV POETRY_HOME="/opt/poetry"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Рабочая директория
WORKDIR /app

# Копируем только pyproject и lock-файл для кеша
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости без установки проекта
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

# Копируем весь проект
COPY ./src /app/src

# Работаем из src/
WORKDIR /app/src

# Открываем порт
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
