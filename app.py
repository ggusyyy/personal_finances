from dotenv import load_dotenv
from fastapi import FastAPI

from src.auth.api.auth_routes import router as auth_routes
from src.users.api.user_routes import router as user_router

load_dotenv()

app = FastAPI(
    title="Personal Finance App",
    description="An application to manage personal finances",
    version="1.0.0"
)

@app.get("/")
async def home() -> dict[str, str]:
    return {"message": "Welcome to the Personal Finance App!"}

app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(auth_routes, prefix="/api", tags=["auth"])