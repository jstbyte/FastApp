from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from app.auth.service import AccessToken, encode_token
from app.auth.service import password_verify
from app.auth.model import User
from app.database import SessDB


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/token", response_model=AccessToken)
def token(db: SessDB, form: OAuth2PasswordRequestForm = Depends()):
    user = db.exec(select(User).where(User.email == form.username)).first()
    if user and password_verify(form.password, user.password):
        user_dict = user.model_dump(exclude={"password"})  # Plain dict;
        return {"access_token": encode_token(user_dict), "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials!")
