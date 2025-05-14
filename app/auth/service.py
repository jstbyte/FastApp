from datetime import datetime, timezone as tz, timedelta as tdelta
from fastapi.security import OAuth2PasswordBearer
import os, jwt, bcrypt  # noqa: E401
from pydantic import BaseModel
from fastapi import Security
from typing import Annotated


_JWT_ALGORITHM = "HS256"
_JWT_SECRAT_KEY = os.getenv("JWT_SECRAT_KEY", "d32y78dN")

OA2Token = OAuth2PasswordBearer(tokenUrl="auth/token")
AuthToken = Annotated[str, Security(OA2Token)]  # type;


class AccessToken(BaseModel):  # Access Token for JWT;
    access_token: str
    token_type: str


def encode_token(payload: dict, exp_mnt=60 * 12, key=_JWT_SECRAT_KEY):
    payload["exp"] = datetime.now(tz=tz.utc)  # get the  Current Time;
    payload["exp"] += tdelta(minutes=exp_mnt)  # Add  Expiration Time;
    return jwt.encode(payload, key, _JWT_ALGORITHM)


def decode_token(token: str, key=_JWT_SECRAT_KEY) -> dict:
    return jwt.decode(token, key, algorithms=[_JWT_ALGORITHM])


def password_hash(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()  # Generate a Random Salt;
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")


def password_verify(password: str, hashed_password: str) -> bool:
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
