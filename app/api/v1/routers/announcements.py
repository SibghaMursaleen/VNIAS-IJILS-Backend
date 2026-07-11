# app/api/v1/routers/announcements.py
from fastapi import APIRouter
from app.core.cache import get_cached_data, set_cached_data

router = APIRouter(prefix='/announcements', tags=['Announcements'])

@router.get('/latest')
async def get_latest_announcements():
    cache_key = "announcements:latest"
    
    # 1. Try fetching from rapid memory cache first
    cached_payload = await get_cached_data(cache_key)
    if cached_payload:
        return {"source": "Redis Memory Cache", "data": cached_payload}
        
    # 2. If not found in cache, simulate fetching from a slow database
    print("[SERVER] Cache Miss! Querying database records...")
    db_mock_data = [
        {"id": 1, "title": "VNIAS Call for Papers 2026", "priority": "high"},
        {"id": 2, "title": "System Maintenance Scheduled for Sunday", "priority": "low"}
    ]
    
    # 3. Store the result into Redis so the NEXT request is lightning fast
    await set_cached_data(cache_key, db_mock_data, expire_seconds=300)
    
    return {"source": "Database Storage Engine", "data": db_mock_data}