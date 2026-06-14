# Task Manager API

REST API для управления задачами, построенный на FastAPI и PostgreSQL.

## Технологии
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

## Endpoints
- GET /tasks — получить все задачи
- POST /tasks — создать задачу
- PUT /tasks/{id}/complete — отметить выполненной
- DELETE /tasks/{id} — удалить задачу

## Запуск

1. Установи зависимости:
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

2. Создай файл .env:
DATABASE_URL=postgresql://postgres:пароль@localhost:5432/taskmanager

3. Запусти сервер:
python -m uvicorn api:app --reload

4. Открой документацию:
http://127.0.0.1:8000/docs