from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from users.application.dtos.create_user_dto import CreateUserDTO
from users.application.use_cases.get_all_users_use_case import GetAllUsersUseCase
from users.application.use_cases.get_user_by_id_use_case import GetUserByIdUseCase

from .deps import get_create_user_use_case, get_list_all_users_use_case, get_user_by_id_use_case
from .schemas import UserCreate, UserOut
from ..application.use_cases.create_user_use_case import CreateUserUseCase
from users.domain.user import User


router = APIRouter()

@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(
    new_user: UserCreate,
    create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    """
    endpoint to create a new user
    """

    try:
        user: User = create_user_use_case.run(
            CreateUserDTO(
            username=new_user.username,
            email=new_user.email,
            password=new_user.password
            )
        )


    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    return UserOut(
        id=user.id,
        username=user.username,
        email=str(user.email)
    )

@router.get("/users/", response_model=List[UserOut])
def get_all_users(
    get_all_users_use_case: GetAllUsersUseCase = Depends(get_list_all_users_use_case)
    ):
    """
    endpoint to get all users
    """
    users: List[UserOut] = get_all_users_use_case.run()
    
    return users

@router.get("/users", response_model=UserOut)
def get_user_by_id(
    id: str,
    get_user_by_id_use_case: GetUserByIdUseCase = Depends(get_user_by_id_use_case)
):
    """
    endpoint to get a user by id
    """
    user: UserOut = get_user_by_id_use_case.run(id) # ARREGLA ESTO

    return user