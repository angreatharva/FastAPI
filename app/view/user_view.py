from fastapi import APIRouter, HTTPException
from app.controller.user_controller import (
    get_all_users,
    create_user,
    get_user_by_id,
    update_user,
    delete_user
)
from app.model import User
from typing import List

router = APIRouter()

# Get all users
@router.get("/users/", response_model=List[User])
async def get_users():
    users = await get_all_users()
    return users

# Create a new user
@router.post("/users/", response_model=User)
async def create_new_user(user: User):
    user_data = user.dict()  # Convert Pydantic model to dict
    new_user = await create_user(user_data)
    return new_user

# Get a user by ID
@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Update a user by ID
@router.put("/users/{user_id}", response_model=User)
async def update_user_info(user_id: str, user: User):
    user_data = user.dict()
    updated_user = await update_user(user_id, user_data)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user by ID
@router.delete("/users/{user_id}", response_model=dict)
async def delete_user_info(user_id: str):
    success = await delete_user(user_id)
    if success:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
