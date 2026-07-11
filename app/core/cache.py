# app/core/cache.py
import json

# A simple Python dictionary acting as our temporary in-memory Redis database
_mock_redis_storage = {}

async def get_cached_data(key: str) -> dict | None:
    """Retrieve data from our mock in-memory storage."""
    if key in _mock_redis_storage:
        print(f"[CACHE] Lightning Hit! Found data in memory for key: {key}")
        return json.loads(_mock_redis_storage[key])
    return None

async def set_cached_data(key: str, value: dict, expire_seconds: int = 300):
    """Store data inside our mock in-memory storage."""
    _mock_redis_storage[key] = json.dumps(value)
    print(f"[CACHE] Stored data in memory for key: {key} (Expires in {expire_seconds}s)")