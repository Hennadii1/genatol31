import psycopg2

class DataBase:

    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = '127.0.0.1'
        self.db_port = 5432


    def __enter__(self):

        self.conn = psycopg2.connect(dbname=self.db_name, user=self.db_user, password=self.db_password, host=self.db_host, port=self.db_port)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.conn.close()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass



with DataBase('users', 'my_user1', '123') as db:
    print('ok')
