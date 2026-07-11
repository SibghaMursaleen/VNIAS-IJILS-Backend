
# app/core/exceptions.py

class ManuscriptNotFoundError(Exception):
    def __init__(self, manuscript_id: int):
        self.manuscript_id = manuscript_id

class DuplicateEmailError(Exception):
    def __init__(self, email: str):
        self.email = email

class UnauthorizedRoleError(Exception):
    def __init__(self, required_roles: list[str], current_role: str):
        self.required_roles = required_roles
        self.current_role = current_role

class StorageUploadError(Exception):
    def __init__(self, message: str):
        self.message = message

class ReviewerAlreadyAssignedError(Exception):
    def __init__(self, manuscript_id: int, reviewer_id: int):
        self.manuscript_id = manuscript_id
        self.reviewer_id = reviewer_id