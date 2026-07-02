import logging

class MockAsyncSession:
    async def commit(self):
        pass
    async def close(self):
        print("\n**************************************************")
        print("[DATABASE] AsyncSessionLocal successfully closed.")
        print("**************************************************\n")

async def get_db():
    print("\n**************************************************")
    print("[DATABASE] Request received: Opening fresh AsyncSessionLocal...")
    print("**************************************************\n")
    session = MockAsyncSession()
    try:
        yield session
    finally:
        await session.close()