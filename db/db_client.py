import sqlite3

class DbClient:
    def __init__(self, db_path='test_data.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_posts_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            body TEXT
        )
        """
        self.cursor.execute(query)
        self.connection.commit()

if __name__ == '__main__':
    db = DbClient()
    db.create_posts_table()
    print("База данных и таблица успешно созданы!")