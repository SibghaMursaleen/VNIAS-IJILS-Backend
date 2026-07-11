# app/api/v1/routers/errors_test.py
from fastapi import APIRouter
from app.core.exceptions import (
    ManuscriptNotFoundError,
    DuplicateEmailError,
    UnauthorizedRoleError,
    StorageUploadError,
    ReviewerAlreadyAssignedError
)

router = APIRouter(prefix='/test-errors', tags=['Exception Testing Module'])

@router.get('/trigger-404')
async def trigger_manuscript_missing():
    # Deliberately throwing the error with a sample ID
    raise ManuscriptNotFoundError(manuscript_id=101)

@router.get('/trigger-409-email')
async def trigger_duplicate_email():
    raise DuplicateEmailError(email="test_author@vnias.org")

@router.get('/trigger-403')
async def trigger_role_violation():
    raise UnauthorizedRoleError(required_roles=["managing_editor", "administrator"], current_role="author")

@router.get('/trigger-500')
async def trigger_storage_crash():
    raise StorageUploadError(message="WP Arena storage disk partition is full. Write operation aborted.")

@router.get('/trigger-409-reviewer')
async def trigger_reviewer_conflict():
    raise ReviewerAlreadyAssignedError(manuscript_id=505, reviewer_id=99)