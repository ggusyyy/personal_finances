import logging
from typing import List
from fastapi import APIRouter, status, Depends, HTTPException

from src.users.application.use_cases.get_all_users_use_case import GetAllUsersUseCase
from src.users.application.use_cases.get_user_by_id_use_case import GetUserByIdUseCase
from src.users.api.schemas import UserOut

from .deps import get_list_all_users_use_case, get_user_by_id_use_case


router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/users/", response_model=List[UserOut])
def get_all_users(
    get_all_users_use_case: GetAllUsersUseCase = Depends(get_list_all_users_use_case)
    ):
    """
    Endpoint to get all users
    """
    try:
        users: List[UserOut] = get_all_users_use_case.run()
    except Exception as e:
        logging.error(f"Error getting users: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error getting users"
        )

    return users

@router.get("/users", response_model=UserOut)
def get_user_by_id(
    id: str,
    get_user_by_id_use_case: GetUserByIdUseCase = Depends(get_user_by_id_use_case)
):
    """
    Endpoint to get a user by id
    """
    try:
        user: UserOut = get_user_by_id_use_case.run(id)
    except Exception as e:
        logging.error(f"Error getting user: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error getting user"
        )

    return user