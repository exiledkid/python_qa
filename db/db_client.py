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

    def add_post(self, title: str, body: str) -> int:
        # SQL-запрос на вставку. Знаки ? — это безопасные подстановки
        query = "INSERT INTO posts (title, body) VALUES (?, ?)"
        self.cursor.execute(query, (title, body))
        self.connection.commit()
        # Возвращаем ID только что созданной строки
        return self.cursor.lastrowid

    def get_post_by_id(self, post_id: int):
        # SQL-запрос на выборку строки по её ID
        query = "SELECT id, title, body FROM posts WHERE id = ?"
        self.cursor.execute(query, (post_id,))
        # fetchone() забирает одну найденную строку из базы
        return self.cursor.fetchone()

# --- ПРОВЕРКА МЕХАНИКИ ---
if __name__ == '__main__':
    db = DbClient()
    db.create_posts_table()
    
    # 1. Записываем новый пост в базу
    new_id = db.add_post(title="Тестовый заголовок", body="Тестовый текст поста")
    print(f"Запись добавлена! Присвоен ID: {new_id}")
    
    # 2. Читаем этот же пост из базы
    saved_post = db.get_post_by_id(new_id)
    print(f"Прочитано из базы: {saved_post}")