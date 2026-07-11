import time
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

# Import configuration settings and routers
from app.core.config import settings
from app.api.v1.routers import users, manuscripts, announcements, errors_test

# Import your brand-new custom errors
from app.core.exceptions import (
    ManuscriptNotFoundError,
    DuplicateEmailError,
    UnauthorizedRoleError,
    StorageUploadError,
    ReviewerAlreadyAssignedError
)

app = FastAPI(title="VNIAS-IJILS Backend API - Phase 0 Scaffold")

# =========================================================================
# --- Security: CORS Middleware Configuration ---
# =========================================================================
# Split the comma-separated origins string from your .env file into a clean list
origins = [origin.strip() for origin in settings.allowed_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# =========================================================================
# --- Request Lifecycle: Custom Performance Logging Middleware ---
# =========================================================================
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    print(f"[LOG] {request.method} {request.url.path} - Status: {response.status_code} ({process_time:.2f}ms)")
    return response

# =========================================================================
# --- Application Routers Registration ---
# =========================================================================
app.include_router(users.router, prefix="/api/v1")
app.include_router(manuscripts.router, prefix="/api/v1")
app.include_router(announcements.router, prefix="/api/v1")
app.include_router(errors_test.router, prefix="/api/v1")  # Exception testing suite

@app.get("/")
async def root():
    return {"message": "VNIAS-IJILS Phase 0 Core Scaffold Running Successfully"}


# =========================================================================
# --- New Week 2 Global Exception Handlers ---
# =========================================================================

# 1. Catching Manuscript Missing Error (404)
@app.exception_handler(ManuscriptNotFoundError)
async def manuscript_not_found_handler(request: Request, exc: ManuscriptNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": "MANUSCRIPT_NOT_FOUND", "message": f"No manuscript with ID {exc.manuscript_id} exists."}
    )

# 2. Catching Duplicate Registration Emails (409)
@app.exception_handler(DuplicateEmailError)
async def duplicate_email_handler(request: Request, exc: DuplicateEmailError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"error": "DUPLICATE_EMAIL", "message": f"The email '{exc.email}' is already registered."}
    )

# 3. Catching Role Violations (403)
@app.exception_handler(UnauthorizedRoleError)
async def unauthorized_role_handler(request: Request, exc: UnauthorizedRoleError):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "error": "INSUFFICIENT_ROLE", 
            "message": "You do not have permission to access this resource.",
            "required": exc.required_roles,
            "current": exc.current_role
        }
    )

# 4. Catching Storage System Failures (500)
@app.exception_handler(StorageUploadError)
async def storage_upload_handler(request: Request, exc: StorageUploadError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "STORAGE_UPLOAD_ERROR", "message": exc.message}
    )

# 5. Catching Double-Booking Reviewer Conflicts (409)
@app.exception_handler(ReviewerAlreadyAssignedError)
async def reviewer_assignment_handler(request: Request, exc: ReviewerAlreadyAssignedError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "REVIEWER_ALREADY_ASSIGNED", 
            "message": f"Reviewer {exc.reviewer_id} is already assigned to manuscript {exc.manuscript_id}."
        }
    )

# 6. Overriding default Pydantic Request Validation Responses (422)
@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        content={"error": "VALIDATION_FAILED", "errors": errors}
    )