from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.application.dtos.login_dto import LoginDTO
from src.auth.application.use_cases.login_user_use_case import LoginUserUseCase
from src.auth.domain.auth_token import AuthToken
from src.auth.api.deps import get_login_user_use_case, get_register_user_use_case
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
) -> UserOut:
    """
    Endpoint to create a new user
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


@router.post("/login", response_model=str)
def login_user(
    login_dto: LoginDTO,
    use_case: LoginUserUseCase = Depends(get_login_user_use_case)
    ) -> str:
    """
    Endpoint to log in a user and return a JWT token
    """

    try:
        token: AuthToken = use_case.run(login_dto)
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    
    return token.content