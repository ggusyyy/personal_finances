import os
from contextlib import contextmanager
from typing import Generator
from psycopg2.pool import SimpleConnectionPool
from psycopg2 import DatabaseError
from psycopg2.extensions import connection as Connection 
from dotenv import load_dotenv

load_dotenv()

__pool: SimpleConnectionPool | None = None

def init_pool(dsn: str | None = None, minconn: int = 1, maxconn: int = 5) -> None:
    global __pool
    if __pool is None:
        dsn = dsn or os.getenv("DATABASE_URL")
        if not dsn:
            raise RuntimeError("DATABASE_URL no configurado")
        __pool = SimpleConnectionPool(minconn, maxconn, dsn)

def close_pool() -> None:
    global __pool
    if __pool:
        __pool.closeall()
        __pool = None

@contextmanager
def db_conn() -> Generator[Connection, None, None]:
    """cede una conexión del pool y la devuelve automáticamente."""
    global __pool
    if not __pool :
        init_pool()
        
    
    conn = __pool.getconn() 
    try:
        yield conn
    except DatabaseError:
        conn.rollback()
        raise
    finally:
        __pool.putconn(conn)
