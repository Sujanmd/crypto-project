from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import hashlib

SECRET_KEY = "your-secret-key"  # move to env later
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MAX_BCRYPT_BYTES = 72


def _normalize_password(password: str) -> str:
    password = str(password)
    if len(password.encode("utf-8")) > MAX_BCRYPT_BYTES:
        # Hash long passwords first (safe & recommended)
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    return password


def hash_password(password: str) -> str:
    password = _normalize_password(password)
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    plain = _normalize_password(plain)
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
