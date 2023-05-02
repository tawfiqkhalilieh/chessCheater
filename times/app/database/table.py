from botocore.exceptions import ClientError
from psycopg2 import sql
from app.database import aurora

class Table:

    def create_tables(self):
        try:
            aurora.query(sql.SQL(open('app/database/create-scripts/times.sql', 'r').read()))
        except ClientError as e:
            print(e)

    def drop_tables(self):
        try:
            aurora.query(sql.SQL(open('app/database/drop-scripts/times.sql', 'r').read()))
        except ClientError as e:
            raise e
        
table = Table()