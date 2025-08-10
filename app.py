from fastapi import FastAPI

from users.api.user_routes import router as user_router

app = FastAPI(
    title="Personal Finance App",
    description="An application to manage personal finances",
    version="1.0.0"
)

@app.get("/")
async def home() -> dict[str, str]:
    return {"message": "Welcome to the Personal Finance App!"}

app.include_router(user_router, prefix="/api", tags=["users"])