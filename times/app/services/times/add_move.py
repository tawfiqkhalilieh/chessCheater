from psycopg2 import sql
from app.database import aurora
from typing import Optional

def add_move(move: int, color: str, value: float):
    return aurora.query(sql.SQL(
            f"UPDATE times SET {color} = ARRAY_APPEND({color},'{value}') WHERE id={move}"
        )).json()