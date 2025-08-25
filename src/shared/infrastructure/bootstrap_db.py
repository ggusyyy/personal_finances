from src.shared.infrastructure.postgres import db_conn
from src.users.infrastructure.queries.postgres import UserPostGresQueries as user_queries
from src.transactions.infrastructure.queries.postgres import TransactionPostgresQueries as transaction_queries

def bootstrap_db():
    with db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(user_queries.CREATE_TABLE.value)
            cur.execute(transaction_queries.CREATE_TABLE.value)
        conn.commit()
