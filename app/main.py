import time
from fastapi import FastAPI, Request
# CRITICAL: Make sure manuscripts is explicitly imported from your routers folder!
from app.api.v1.routers import users, manuscripts, announcements

app = FastAPI(title="VNIAS-IJILS Backend API - Phase 0 Scaffold")

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    print(f"[LOG] {request.method} {request.url.path} - Status: {response.status_code} ({process_time:.2f}ms)")
    return response

# Register the routers explicitly under the v1 sub-path
app.include_router(users.router, prefix="/api/v1")
app.include_router(manuscripts.router, prefix="/api/v1")
app.include_router(announcements.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "VNIAS-IJILS Phase 0 Core Scaffold Running Successfully"}