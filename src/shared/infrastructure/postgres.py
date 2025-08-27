from functools import lru_cache
import os
from contextlib import contextmanager
from typing import Generator
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import connection as Connection 
from dotenv import load_dotenv

load_dotenv()

@lru_cache(maxsize=1)
def get_pool() -> SimpleConnectionPool:
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        raise RuntimeError("DATABASE_URL no configurado")
    minconn = int(os.getenv("DB_MINCONN", "1"))
    maxconn = int(os.getenv("DB_MAXCONN", "5"))
    return SimpleConnectionPool(minconn, maxconn, dsn)

def close_pool() -> None:
    # Llamar en el shutdown de la app (signal, atexit, hook del framework, etc.)
    pool = get_pool()          # obtiene el único pool cacheado
    pool.closeall()            # cierra todas las conexiones
    get_pool.cache_clear()     # limpia la caché para permitir una futura recreación

@contextmanager
def db_conn() -> Generator[Connection, None, None]:
    pool = get_pool()
    conn = pool.getconn()
    try:
        yield conn
        conn.commit()          # commit en la ruta de éxito
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass               # si no hay transacción abierta, ignoramos
        raise
    finally:
        pool.putconn(conn)
