from typing import List, Optional
from src.shared.infrastructure.postgres import db_conn
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository
from src.users.domain.value_objects.email import Email
from src.users.infrastructure.queries.postgres import UserPostGresQueries as queries

class PostgresUserRepository(UserRepository):
    def save(self, user: User) -> None:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.INSERT_USER.value,
                (user.id,
                 user.username,
                 str(user.email),
                 user.password,
                 user.created_at,
                 user.balance)
            )
            conn.commit()

    def get_by_id(self, id: str) -> Optional[User]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_BY_ID.value,
                (id,)
                )
            row = cur.fetchone()
            return User(*row) if row else None

    def get_by_username(self, username: str) -> Optional[User]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_BY_USERNAME.value,
                (username,)
                )
            row = cur.fetchone()
            return User(*row) if row else None

    def get_by_email(self, email: Email) -> Optional[User]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_BY_EMAIL.value,
                (str(email),)
                )
            row = cur.fetchone()
            return User(*row) if row else None

    def get_all(self) -> List[User]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_ALL.value
                )
            rows = cur.fetchall()
            return [User(*r) for r in rows]

    def change_password(self, new_password: str, user_id: str) -> None:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.UPDATE_PASSWORD.value,
                (new_password, user_id)
                )
            conn.commit()

    def delete(self, id: str) -> None:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(queries.DELETE_USER.value, (id,))
            conn.commit()
