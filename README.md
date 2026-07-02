<h1 align="center">🔷 VNIAS-IJILS Backend API</h1>

<p align="center">
  A high-performance FastAPI backend scaffolding user, manuscript, and announcement services for the VNIAS-IJILS platform.<br/>
  Designed with clean architecture, dependency injection, and scalable routing.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/FastAPI-0.110.0+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
</p>

---

## 📌 Overview

The **VNIAS-IJILS Backend API** serves as the core web service for managing the VNIAS-IJILS application lifecycle. It exposes RESTful APIs for **user registration/management**, **manuscript submissions**, and **platform announcements**. Utilizing a scaffolded architecture, it allows rapid scaling of business repositories and clean separation of schemas and models.

> **Note:** The current state represents a **Phase 0 Scaffold** configured with mock async database dependencies for testing the routing flow.

---

## ⚙️ How It Works

| Step | Stage | Description |
|------|-------|-------------|
| 1 | **Request Interception** | HTTP middleware captures all incoming client requests to compute and log execution times. |
| 2 | **Routing** | FastAPI `APIRouter` dispatches endpoints dynamically under the `/api/v1` prefix. |
| 3 | **Dependency Injection** | The `get_db` generator yields a mock database session to simulate safe database transactions. |
| 4 | **Response Generation** | Structured JSON responses are returned to the client conforming to validation schemas. |

---

## 📁 Project Structure

```
vnias_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routers/
│   │           ├── announcements.py   # Announcement endpoints
│   │           ├── auth.py            # Authentication & token endpoints
│   │           ├── manuscripts.py     # Manuscript submission & retrieval
│   │           └── users.py           # User management
│   ├── core/
│   │   ├── config.py                  # App configuration settings
│   │   ├── dependencies.py            # FastAPI dependency injectors
│   │   └── security.py                # Security & hashing utilities
│   ├── models/                        # SQL Alchemy database models (Placeholder)
│   ├── repositories/                  # Data access layer classes (Placeholder)
│   ├── schemas/                       # Pydantic schemas (Placeholder)
│   └── main.py                        # FastAPI application entrypoint
├── .gitignore                         # Git exclusion rules
├── requirements.txt                   # Project package dependencies
└── README.md                          # Documentation
```

> **Note:** The `.venv` environment directory is ignored to keep the repository lightweight. Run environment setup to recreate it locally.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10** or higher
- **Git**

#### Step 1: Clone the repository

```bash
git clone https://github.com/SibghaMursaleen/VNIAS-IJILS-Backend.git
cd VNIAS-IJILS-Backend
```

#### Step 2: Create a virtual environment and activate it

```bash
python -m venv .venv
```

Activation on Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Activation on macOS/Linux:
```bash
source .venv/bin/activate
```

#### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

#### Step 5: Verify the running server

```bash
curl http://127.0.0.1:8000/
```

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **FastAPI** | High-performance modern web framework for building APIs with Python. |
| **Uvicorn** | Fast ASGI web server implementation used to run the application. |
| **Pydantic** | Data validation and settings management using Python type annotations. |

---

## ⚠️ Tips / Best Practices

- Always activate the virtual environment (`.venv`) before running the API or installing packages.
- Follow the router architecture under `app/api/v1/routers` to keep endpoint files modular.
- Implement business logic under `app/repositories` and datatypes under `app/schemas` rather than inside router files.
- Inject database sessions using FastAPI's `Depends(get_db)` to ensure connection pooling and automated cleanup.

---

## 📄 License

This project is released under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

<p align="center">
  Built with 🐍 Python &nbsp;·&nbsp; Efficient Academic Journal APIs
</p>
