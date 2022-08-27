import pymssql


class Database:

    def __init__(self, host, port, username, password) -> None:
        self.connection = pymssql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
        )

    def execute(self, query: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res
