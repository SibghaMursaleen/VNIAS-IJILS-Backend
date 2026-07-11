<h1 align="center">🔷 VNIAS-IJILS Backend API</h1>

<p align="center">
  A high-performance FastAPI backend scaffolding user, manuscript, and announcement services for the VNIAS-IJILS platform.<br/>
  Designed with clean architecture, dependency injection, and scalable routing.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.110.0+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
</p>

---

## 📌 Overview

The **VNIAS-IJILS Backend API** is the core web service for managing the VNIAS-IJILS academic publishing platform. It exposes modular RESTful APIs for **user management**, **manuscript submission**, and **announcements**. 

> **The Big Picture:** The codebase is organized such that each layer has a distinct, isolated responsibility. This architectural choice prevents messy code and makes it easy to maintain or scale the platform as new publishing services are introduced.

---

## ⚙️ How It Works

| Step | Stage | Description |
|------|-------|-------------|
| 1 | **Request Interception** | Custom `logging_middleware` intercepts incoming HTTP **requests** to track performance benchmarks and log statuses. |
| 2 | **Validation & Security** | Payloads are validated via Pydantic `BaseModel` schemas, and sensitive values (e.g., passwords) are hashed using `bcrypt`. |
| 3 | **Routing & Dispatch** | FastAPI router dispatches the request to the matching controller endpoint under the `/api/v1` namespace. |
| 4 | **Data & Layer Access** | The database connection or cache is accessed using the `ManuscriptRepository` pattern and async database pool. |
| 5 | **Exception Handling** | Any application exceptions are caught globally by the custom handlers and mapped to standard JSON structures. |
| 6 | **Storage Pipeline** | Incoming manuscript documents are streamed directly to `wp_arena_storage` to keep RAM consumption low. |

---

## 📅 Weekly Milestones

### 🕒 Week 1: The Core Infrastructure Foundations
During the opening week, the focus was on setting up the initial network routing, web server pipelines, and request monitoring systems:

| Feature Area | Component | Description | Key Files |
|--------------|-----------|-------------|-----------|
| **Asynchronous Route Scaffold** | Network Routing | Created decoupled endpoints for users, manuscripts, and announcements. | `app/api/v1/routers/` |
| **Performance Logging Middleware** | Request Monitoring | Engineered a custom interceptor that computes HTTP request execution times in milliseconds ($ms$) and logs status codes. | `app/main.py` |
| **Uvicorn Web Server Integration** | Web Hosting Pipeline | Established the local hosting configuration running on port `8080` with hot-reloading active. | Root setup |

### 🔒 Week 2: Advanced Security, Repositories, & Fail-Safes
This milestone introduced security firewalls, memory optimization, data abstraction layers, and unified exception systems:

| Feature Area | Component | Description | Key Files |
|--------------|-----------|-------------|-----------|
| **Type-Safe Environment Variables** | Security & Configuration | Built a fast-failing configuration loader using `pydantic-settings` to block startup if environment variables are missing. | `app/core/config.py` |
| **Dynamic CORS Security** | Security & Configuration | Integrated a dynamic domain firewall using FastAPI `CORSMiddleware`, reading origins from custom parameters. | `app/main.py` |
| **Native Cryptographic Encryption** | Security & Configuration | Implemented secure, one-way password hashing using native `bcrypt` binaries to scramble user credentials. | `app/core/security.py` |
| **The Repository Pattern** | Data & Memory Performance | Decoupled database operations from routers into the `ManuscriptRepository` class. | `app/repositories/manuscript_repo.py` |
| **Asynchronous Database Pooling** | Data & Memory Performance | Configured an async database session factory `get_db` using `SQLAlchemy` to support warm connection pools. | `app/core/dependencies.py` |
| **Fast In-Memory Caching** | Data & Memory Performance | Designed a simulated Redis key-value cache manager to serve repetitive data instantly from memory. | `app/core/cache.py` |
| **Global Exception Management** | File Handling & Fail-Safes | Registered six centralized global exception handlers in `main.py` to map custom exceptions into structured JSON responses. | `app/core/exceptions.py`, `app/main.py` |
| **WP Arena Streaming Storage Sandbox** | File Handling & Fail-Safes | Created a file upload handler that streams incoming files straight to disk storage to prevent RAM bloat. | `app/core/storage.py`, `app/api/v1/routers/manuscripts.py` |

---

## 📁 Project Structure

```
vnias_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routers/
│   │           ├── announcements.py   # Announcement endpoints with memory caching
│   │           ├── auth.py            # Authentication & token endpoints (stubbed)
│   │           ├── errors_test.py     # Exception validation testing suite
│   │           ├── manuscripts.py     # Manuscript submission & retrieval
│   │           └── users.py           # User registration and encryption
│   ├── core/
│   │   ├── cache.py                  # In-memory mock Redis key-value cache
│   │   ├── config.py                  # Pydantic-settings type-safe configuration loader
│   │   ├── dependencies.py            # Async database connection pooling
│   │   ├── exceptions.py              # Custom project-specific exception models
│   │   ├── security.py                # BCrypt one-way password hashing
│   │   └── storage.py                 # File handler & streaming sandbox directory
│   ├── models/
│   │   └── .gitkeep                   # Database schema models directory
│   ├── repositories/
│   │   ├── .gitkeep                   # Data access repository indicators
│   │   └── manuscript_repo.py         # ManuscriptRepository data handler
│   ├── schemas/
│   │   ├── .gitkeep                   # Pydantic schema validation base
│   │   ├── manuscripts.py             # Manuscript validation schemas
│   │   └── users.py                   # User registration schemas
│   └── main.py                        # FastAPI entrypoint & global exception mappings
├── wp_arena_storage/                  # Uploaded manuscripts storage directory
├── .env                               # Environment configurations (git-ignored)
├── .gitignore                         # Git exclusion rules
├── LICENSE                            # MIT License file
├── requirements.txt                   # Project package dependencies
└── README.md                          # Repository documentation
```

> **Note:** The `.venv` virtual environment directory and the `.env` file are excluded from the repository. Follow the steps below to configure your `.env` configuration.

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

#### Step 4: Configure environment variables

Create a `.env` file in the root directory and populate the required parameters:

```ini
DB_URL=mysql+aiomysql://root:password@localhost:3306/vnias_db
REDIS_URL=redis://localhost:6379/0
ZEPTOMAIL_TOKEN=your_mock_zeptomail_api_token_here
SECRET_KEY=super_secret_vnias_jwt_signing_key_2026
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

#### Step 5: Run the FastAPI application

```bash
uvicorn app.main:app --reload --port 8080
```

#### Step 6: Verify the running server

```bash
curl http://127.0.0.1:8080/
```

---

## 🎨 Configuration

| Environment Key | Type | Purpose / Description | Default / Example Value | Status |
|-----------------|------|-----------------------|-------------------------|--------|
| `DB_URL` | `str` | Connection string for asynchronous MySQL/MariaDB database pooling. | `mysql+aiomysql://root:password@localhost:3306/vnias_db` | ✅ Active |
| `REDIS_URL` | `str` | Connection string for cache engine integration. | `redis://localhost:6379/0` | ✅ Active |
| `ZEPTOMAIL_TOKEN` | `str` | API authorization token for mail delivery. | `your_mock_zeptomail_api_token_here` | ✅ Active |
| `SECRET_KEY` | `str` | Secret string key used for cryptographically signing JWT authentication tokens. | `super_secret_vnias_jwt_signing_key_2026` | ✅ Active |
| `ALLOWED_ORIGINS` | `str` | Comma-separated list of permitted web application client addresses for CORS filter. | `http://localhost:3000,http://127.0.0.1:3000` | ✅ Active |

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **Python 3.10+** | Base programming language for core implementation logic. |
| **FastAPI** | High-performance, modern ASGI web framework for Python. |
| **Uvicorn** | ASGI server wrapper running local development hosting pipelines. |
| **Pydantic v2** | Core schema parsing, field coercion, and settings validation. |
| **SQLAlchemy** | Async engine driver and Object Relational Mapper (ORM) base. |
| **BCrypt** | Native binary hashing algorithms for cryptographically secure passwords. |
| **aiomysql** | Async MySQL driver utilized for non-blocking database operations. |
| **python-multipart** | Native parsing engine handling incoming multipart form data streams. |

---

## ⚠️ Tips / Best Practices

- Always keep **environment variables** populated in `.env`; missing keys will trigger a **fail-fast startup check** that halts the server.
- Follow the **layer isolation** design rules: write schemas in `app/schemas/`, database access in `app/repositories/`, and controllers in `app/api/v1/routers/`.
- Use the `Depends(get_db)` utility to inject session contexts safely and leverage automatic connection pool disposal.
- When uploading files, ensure incoming payloads are sent as `multipart/form-data` and bounded to extensions (`.pdf`, `.docx`, `.doc`).

---

## 📄 License

This project is released under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

<p align="center">
  Built with 🐍 Python &nbsp;·&nbsp; Efficient Academic Journal APIs
</p>
