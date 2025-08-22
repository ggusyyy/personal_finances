from dotenv import load_dotenv
from fastapi import FastAPI

from src.auth.api.auth_routes import router as auth_routes
from src.users.api.user_routes import router as user_routes
from src.transactions.api.transactions_routes import router as transaction_routes

load_dotenv()

app = FastAPI(
    title="Personal Finance App",
    description="An application to manage personal finances",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {"message": "Welcome to the Personal Finance App!"}

app.include_router(user_routes,         prefix="/api", tags=["users"])
app.include_router(auth_routes,         prefix="/api", tags=["auth"])
app.include_router(transaction_routes,  prefix="/api", tags=["transactions"])