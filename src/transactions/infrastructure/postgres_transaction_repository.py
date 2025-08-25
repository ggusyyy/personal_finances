from typing import List, Optional
from src.shared.infrastructure.postgres import db_conn
from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository
from src.transactions.domain.value_objects.transaction_kind import TransactionKind
from src.transactions.infrastructure.queries.postgres import TransactionPostgresQueries as queries

class PostgresTransactionRepository(TransactionRepository):
    def save(self, transaction: Transaction) -> None:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.INSERT_TRANSACTION.value,
                (transaction.id,
                 transaction.user_id,
                 transaction.concept,
                 transaction.kind.value,
                 transaction.amount,
                 transaction.date)
                )
            conn.commit()

    def get_by_id(self, transaction_id: str) -> Optional[Transaction]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_BY_ID.value,
                (transaction_id,)
                )
            row = cur.fetchone()
            if not row:
                return None
            return Transaction(
                id=row[0],
                user_id=row[1],
                concept=row[2],
                kind=TransactionKind(row[3]),
                amount=row[4],
                date=row[5]
                )

    def get_all_by_user_id(self, user_id: str) -> List[Transaction]:
        with db_conn() as conn, conn.cursor() as cur:
            cur.execute(
                queries.SELECT_ALL_BY_USER_ID.value,
                (user_id,)
                )
            rows = cur.fetchall()
            return [
                Transaction(
                    id=r[0], 
                    user_id=r[1],
                    concept=r[2],
                    kind=TransactionKind(r[3]),
                    amount=r[4],
                    date=r[5])
                for r in rows
                ]