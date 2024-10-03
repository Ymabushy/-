import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('project_freedom.db')

# Создаем объект курсора
cursor = conn.cursor()

# Создаем таблицу для хранения книг
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    content TEXT
)
''')

# Создаем таблицу для хранения статей
cursor.execute('''
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    content TEXT
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных создана успешно.")
