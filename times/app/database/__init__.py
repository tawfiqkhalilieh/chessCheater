import psycopg2
import boto3
from config import settings
from typing import Union
from psycopg2 import sql
from app.services.utils.is_select import is_select
from app.services.utils.QueryFormatter import QueryFormatter

class Aurora:
    _instances = {}
    
    def get_database_parameters(self) -> dict:
        return {
            
        }


    def query(self, sql: Union[sql.SQL, sql.Composed] = None, parameters: Union[list, dict] = []):
        try:
            conn = psycopg2.connect( 
                host=settings.database_host,
                port=settings.database_port,
                dbname=settings.database_default_name,
                user=settings.database_user,
                password=settings.database_password,
                connect_timeout=10
            )

            with conn:
                with conn.cursor() as cur:
                    sql = sql.as_string(cur)
                    cur.execute(query=sql, vars=tuple(parameters) if type(parameters) is list else parameters)
                    if is_select(query=sql):
                        query_results = cur.fetchall()
                        return QueryFormatter(
                            **{"records": query_results, "columns": [ col[0] for col in cur.description if col ]})
                    return QueryFormatter(records=[], columns=[])
        except Exception as e:
            raise e

aurora = Aurora()