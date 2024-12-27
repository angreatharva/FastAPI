from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

# User model to validate and serialize the response data
class User(BaseModel):
    _id: Optional[str]  # ObjectId will be serialized as a string
    username: str
    email: str

    class Config:
        # Use a custom encoder for ObjectId to convert it to a string
        json_encoders = {
            ObjectId: lambda v: str(v)  # Ensure ObjectId is converted to string
        }
