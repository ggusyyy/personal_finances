from enum import Enum


class TransactionPostgresQueries(Enum):
    CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS transactions (
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        concept TEXT NOT NULL,
        kind TEXT NOT NULL,
        amount REAL NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """

    INSERT_TRANSACTION = """
    INSERT INTO transactions (id, user_id, concept, kind, amount, date)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    SELECT_BY_ID = """
    SELECT id, user_id, concept, kind, amount, date
    FROM transactions
    WHERE id = %s;
    """

    SELECT_ALL_BY_USER_ID = """
    SELECT id, user_id, concept, kind, amount, date
    FROM transactions
    WHERE user_id = %s;
    """
