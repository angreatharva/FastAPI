from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "FastApiMongoDB"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]