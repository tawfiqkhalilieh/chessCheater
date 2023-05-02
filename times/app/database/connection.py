from typing import Union
import psycopg2
import sqlparse
from fastapi import HTTPException
from config import settings
from psycopg2 import sql
from app.services.utils.QueryFormatter import QueryFormatter

def execute_statement(sql: Union[sql.SQL, sql.Composed] = None, parameters: Union[list, dict] = []):
    try:
        conn = psycopg2.connect(
            host=settings.rds_endpoint, port=settings.rds_port,
                                database=settings.rds_database, user=settings.rds_user,
                                password=settings.rds_password, connect_timeout=10
            )
        with conn:
            with conn.cursor() as cur:
                sql = sql.as_string(conn)
                # cur.execute(query=sql, vars=tuple(parameters) if type(parameters) is list else parameters)
                cur.execute(query=sql)
                if is_select(query=sql):
                    query_results = cur.fetchall()
                    return QueryFormatter(
                        **{"records": query_results, "columns": [col[0] for col in cur.description]})
                return QueryFormatter(records=[], columns=[])

    except Exception as e:
        raise HTTPException(status_code=400, detail="Database connection failed due to {}".format(e))


def is_select(query: str):
    statements = sqlparse.parse(query)
    for statement in statements:
        if statement.get_type() == "SELECT":
            return True
    return False