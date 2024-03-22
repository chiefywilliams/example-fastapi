from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):   #originally had PostBase in this line and Post in next
    Post: Post
    votes: int



class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None 

class Vote(BaseModel):
    post_id: int
    dir: int #conint(le=1)

class Rank(BaseModel):
    rank_id: int
    rank_name: str
    rank_nato_equiv: str 

class RankCreate(BaseModel):
    rank_name: str
    rank_nato_equiv: str 