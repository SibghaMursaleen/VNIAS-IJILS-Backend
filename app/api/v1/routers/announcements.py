from fastapi import APIRouter

router = APIRouter(prefix='/announcements', tags=['Announcements'])

@router.get('/')
async def get_announcements_stub():
    return {"message": "Announcements fetch stub working"}

@router.post('/')
async def create_announcement_stub():
    return {"message": "Announcement creation stub working"}
