# FastAPI To-Do REST API

A professional, scalable, and future-ready To-Do list REST API built with **FastAPI**, **SQLModel** (async ORM), **SQLite**, and **Alembic** for migrations.

---

## Features

- Async FastAPI application with modular structure  
- SQLite database with SQLModel ORM  
- Alembic migrations for database version control  
- Environment-based configuration using `.env` and `pydantic-settings`  
- Clean architecture with separated layers: models, schemas, repositories, services, routes  
- Data validation with Pydantic schemas  
- Ready for extension to PostgreSQL, Docker, and auth

---

## Project Structure

```
fa-todo-rest/
├── alembic/
│   └── versions/                 # Alembic migration scripts
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/           # FastAPI routes
│   ├── core/
│   │   └── config.py             # App settings (pydantic)
│   ├── crud/ or repositories/    # Data access layer
│   ├── db/
│   │   ├── base.py               # Base metadata
│   │   └── session.py            # DB session management
│   ├── models/                   # SQLModel models
│   ├── schemas/                  # Pydantic schemas
│   ├── services/                 # Business logic layer
│   └── main.py                  # FastAPI app entrypoint
├── .env                         # Environment variables
├── alembic.ini                  # Alembic config
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## Getting Started

### Prerequisites

- Python 3.10+  
- SQLite (comes bundled with Python)

---

### Installation

1. Clone the repo:

```bash
git clone https://github.com/whoismaruf/fa-todo-rest.git
cd fa-todo-rest
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file at project root with:

```env
DATABASE_URL=sqlite+aiosqlite:///./todo.db
API_KEY=your_api_key_here
DEBUG=True
```

5. Run Alembic migrations:

```bash
alembic upgrade head
```

6. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser at http://127.0.0.1:8000/docs for Swagger UI.

---

## Usage

- Create, Read, Update, Delete (CRUD) To-Do items via REST API  
- Use `/docs` for interactive API exploration

---

## Migrations

- To create a new migration after model changes:

```bash
alembic revision --autogenerate -m "your message"
alembic upgrade head
```

---

## Configuration

All settings are managed via environment variables loaded by `pydantic-settings`:

| Variable      | Description           | Default            |
|--------------|-----------------------|--------------------|
| `DATABASE_URL` | Database connection URL | No default (required) |
| `API_KEY`      | API key for auth or external services | No default (required) |
| `DEBUG`       | Enable debug mode (True/False) | False              |

---

## Future Improvements

- Add authentication (JWT, OAuth2)  
- Switch to PostgreSQL or other DBs  
- Dockerize app with Docker Compose  
- Add unit and integration tests  
- Implement pagination, filtering

---

## License

[MIT](LICENSE)

---

## Contact

Created by [Maruf Khan] - feel free to reach out!

---

Happy coding! 🚀
