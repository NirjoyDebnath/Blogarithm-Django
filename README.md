# Blogarithm

A REST API for a blog platform, built with Django and Django REST Framework.

## Features

- Custom user model with email-based authentication
- JWT authentication with access and refresh tokens
- Story (blog post) creation with image upload support
- Swagger and ReDoc API documentation at `/swagger/` and `/redoc/`
- UUID primary keys across all models

## Tech Stack

Python, Django, Django REST Framework, SimpleJWT, drf-yasg, MySQL, Pillow

## Getting Started

**Requirements:** Python 3.12, MySQL

```bash
git clone https://github.com/NirjoyDebnath/Blogarithm-Django.git
cd Blogarithm-Django
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # fill in your values
python manage.py migrate
python manage.py runserver
```

API docs available at `http://localhost:8000/swagger/`

## Endpoints

**Auth**
- `POST /api/token/` — get access + refresh token
- `POST /api/token/refresh/` — refresh access token

**Users**
- `POST /users/signup/` — register
- `POST /users/login/` — login
- `POST /users/logout/` — logout
- `GET /users/` — list users
- `GET/PUT/DELETE /users/{id}/` — user detail

**Stories**
- `GET/POST /story/` — list or create stories
- `GET/PUT/DELETE /story/{id}/` — story detail
