# FastAPI CRUD API

A high-performance, production-ready REST API built with **FastAPI**, featuring full CRUD operations, authentication via JWT, and SQLAlchemy integration.

---

## Features

- 🔒 User authentication with JWT
- 🧾 CRUD operations for blog posts
- 🧠 Data validation using Pydantic
- 🗃️ SQLAlchemy ORM with SQLite (can be extended to PostgreSQL, etc.)
- ⚡ Auto-generated API docs via Swagger UI and ReDoc
- 🧩 Modular architecture with routers


## Project Structure
fastapi-crud-app/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── hashing.py
│ ├── jwt_token.py
│ ├── routers/
│ │ ├── user.py
│ │ ├── blog.py
│ │ └── authentication.py
│ └── oauth2.py
├── requirements.txt
└── README.md
