from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

# Updated User model
class User(BaseModel):
    _id: Optional[str]  # ObjectId will be serialized as a string
    userName: str
    phone: str
    age: int
    gender: str
    email: str
    password: str

    class Config:
        # Use a custom encoder for ObjectId to convert it to a string
        json_encoders = {
            ObjectId: lambda v: str(v)  # Ensure ObjectId is converted to string
        }
