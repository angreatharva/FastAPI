from app.database.connection import db  # Import the db from connection.py
from app.model.user import User
from bson import ObjectId
from typing import List

# Get the users collection from the db
users_collection = db["users"]  # This is the collection you're working with

# Convert ObjectId to string for JSON serialization
def convert_objectid_to_str(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

# Get all users from MongoDB and return them as a list
async def get_all_users() -> List[User]:
    users = await users_collection.find().to_list(length=100)
    return [{**user, "_id": convert_objectid_to_str(user["_id"])} for user in users]

# Create a new user in the MongoDB
async def create_user(user_data: dict) -> User:
    result = await users_collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)
    return User(**user_data)

# Get a single user by ID
async def get_user_by_id(user_id: str) -> User:
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return User(**user)
    return None

# Update a user by ID
async def update_user(user_id: str, user_data: dict) -> User:
    await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_data}
    )
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return User(**user)
    return None

# Delete a user by ID
async def delete_user(user_id: str) -> bool:
    result = await users_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
