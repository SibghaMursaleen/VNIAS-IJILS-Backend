# app/core/dependencies.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

# Initialize the asynchronous database engine with pooling configurations
engine = create_async_engine(
    settings.db_url, 
    pool_pre_ping=True, 
    pool_size=10
)

# Create a session factory for generating localized session workers
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncSession:
    """FastAPI dependency yielding an asynchronous database session lifecycle."""
    async with AsyncSessionLocal() as session:
        yield session  # Ensures the session closes cleanly after the request completes