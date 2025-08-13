from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.api.deps import get_register_user_use_case
from src.auth.api.schemas import UserRegister
from src.auth.application.dtos.register_user_dto import RegisterUserDTO
from src.auth.application.use_cases.register_user_use_case import RegisterUserUseCase
from src.users.api.schemas import UserOut
from src.users.domain.user import User


router = APIRouter()

@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(
    new_user: UserRegister,
    register_user_use_case: RegisterUserUseCase = Depends(get_register_user_use_case)
):
    """
    endpoint to create a new user
    """

    try:
        user: User = register_user_use_case.run(
            RegisterUserDTO(
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