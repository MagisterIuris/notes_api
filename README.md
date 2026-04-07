# 📝 Notes API

A backend API that allows users to create, retrieve, and update their personal notes, with secure authentication using JWT.

---

## 🚀 Tech Stack

- Backend: FastAPI  
- Database: PostgreSQL  
- ORM: SQLAlchemy  
- Validation: Pydantic  
- Authentication: JWT (python-jose)  
- Security: passlib (bcrypt), secrets  
- Containerization: Docker + Docker Compose  

---

## ✨ Features

- User authentication (signup / login)
- JWT token generation
- Notes management:
  - Create notes
  - Retrieve user notes
  - Partially update notes (PATCH)
- User data isolation (security)
- Proper HTTP error handling (401, 404, 422)

---

## 🔐 Security

- Each note is linked to a specific user (user_id)
- Users can only access their own notes
- Authentication is handled via JWT tokens
- Passwords are securely hashed using passlib with the bcrypt algorithm
- Secret keys are generated using Python’s secrets module
- Protection against unauthorized access 

---

## 📦 Setup & Run

### 1. Clone the repository

```bash
git clone <repo_url>
cd <repo>
```

---

### 2. Environment configuration

Rename `.env.example` to `.env`.

#### 🔐 Generate a secret key

Run:

```bash
python scripts/generate_secret_key.py
```

Copy the generated key and paste it into the `.env` file.

---

#### 🧾 Example `.env`

```env
DATABASE_URL=postgresql://notes_api:notes_api@db:5432/notesdb
SECRET_KEY=your_generated_secret_key
```

---

### 3. Run with Docker

```bash
docker-compose up --build
```

---

### 4. Access API docs

http://localhost:8000/docs

---

## 🧠 Architecture

The project follows a layered architecture:

routes → services → repositories → domain → database

- routes: HTTP layer
- services: business logic
- repositories: database access
- domain: SQLAlchemy models
- schemas (DTOs): validation and serialization

---

## 📌 Main Endpoints

### Auth

- POST /users → create a user  
- POST /login → get JWT token  

---

### Notes

- GET /notes → retrieve user notes  
- POST /notes → create a note  
- PATCH /notes/{id} → update a note  

---

## 🐳 Docker

- Two containers:
  - FastAPI backend
  - PostgreSQL database
- Internal communication via Docker network (db as hostname)

---

## 🎯 Project Goals

This project was built to:

- Master backend fundamentals with Python
- Design a secure REST API
- Apply clean architecture (service/repository pattern)
- Use Docker to run a full backend environment

---

## 📈 Future Improvements

- Delete endpoint (DELETE /notes/{id})
- Pagination
- Search / filtering
- Automated tests (Pytest)

---

## 👨‍💻 Author

Aymane Menfaa
