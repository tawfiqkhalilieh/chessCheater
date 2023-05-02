from psycopg2 import sql
from app.database import aurora
from typing import Optional

def get_move(move: Optional[int], color: Optional[str]):
    if not move and not color:
        return aurora.query(sql.SQL(
            f"SELECT * FROM times"
        )).json()
    elif move:
        return aurora.query(sql.SQL(
            f"SELECT * FROM times where id={move}"
        )).json()
    elif color:
        return aurora.query(sql.SQL(
            f"SELECT {color} FROM times"
        )).json()
    else:
        return aurora.query(sql.SQL(
            f"SELECT {color} FROM times where id={id}"
        )).json()
    