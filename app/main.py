from fastapi import FastAPI
from app.view.user_view import router as user_router

app = FastAPI()

# Include the user routes
app.include_router(user_router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the MVC + REST MongoDB API"}