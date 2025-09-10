"""Database utilities for the NCS pipeline."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session


def get_engine():
    url = os.getenv("DB_URL")
    if not url:
        raise RuntimeError("DB_URL not set in environment")
    return create_engine(url)


def get_session() -> Iterator[Session]:
    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        yield session


def init_db() -> None:
    """Execute DDL SQL script to create tables."""
    engine = get_engine()
    ddl_path = Path(__file__).resolve().parents[1] / "sql" / "ddl.sql"
    with open(ddl_path, "r", encoding="utf-8") as f:
        ddl_sql = f.read()
    with engine.begin() as conn:
        for statement in ddl_sql.split(";\n"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))


if __name__ == "__main__":  # pragma: no cover
    init_db()
