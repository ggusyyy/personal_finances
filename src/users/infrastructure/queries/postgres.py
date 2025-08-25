from enum import Enum


class UserPostGresQueries(Enum):
    

    CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        balance REAL DEFAULT 0
    );
    """

    INSERT_USER = """
    INSERT INTO users (id, username, email, password, created_at, balance)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    SELECT_BY_ID = """
    SELECT id, username, email, password, created_at, balance
    FROM users
    WHERE id = %s;
    """

    SELECT_BY_USERNAME = """
    SELECT id, username, email, password, created_at, balance
    FROM users
    WHERE username = %s;
    """

    SELECT_BY_EMAIL = """
    SELECT id, username, email, password, created_at, balance
    FROM users
    WHERE email = %s;
    """

    SELECT_ALL = """
    SELECT id, username, email, password, created_at, balance
    FROM users;
    """

    UPDATE_PASSWORD = """
    UPDATE users
    SET password = %s
    WHERE id = %s;
    """

    DELETE_USER = """
    DELETE FROM users
    WHERE id = %s;
    """
