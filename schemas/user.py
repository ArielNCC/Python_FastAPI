from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserOut(UserBase):
    id: Optional[int]