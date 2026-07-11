# app/core/security.py
import bcrypt

def hash_password(plain_password: str) -> str:
    """Takes a raw password string and returns a secure cryptographic hash using native bcrypt."""
    # Convert plaintext string into bytes
    password_bytes = plain_password.encode('utf-8')
    
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    
    # Return as a decode-safe string block
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compares a raw login password against a stored hash using native bcrypt."""
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    
    return bcrypt.checkpw(password_bytes, hashed_bytes)