from typing import List
from fastapi import APIRouter, status, Depends, HTTPException

from src.users.application.use_cases.get_all_users_use_case import GetAllUsersUseCase
from src.users.application.use_cases.get_user_by_id_use_case import GetUserByIdUseCase
from src.users.api.schemas import UserOut

from .deps import get_list_all_users_use_case, get_user_by_id_use_case


router = APIRouter()


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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
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
        user: UserOut = get_user_by_id_use_case.run(id) # ARREGLA ESTO
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    return user