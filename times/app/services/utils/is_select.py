import sqlparse

def is_select(query: str):
    statements = sqlparse.parse(query)
    for statement in statements:
        if statement.get_type() == "SELECT":
            return True
    return False