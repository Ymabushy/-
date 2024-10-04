import sqlite3

# Функция для подключения к базе данных
def connect_to_db():
    conn = sqlite3.connect('project_freedom.db')
    return conn

# Функция для добавления записи в таблицу users
def add_user(user_id, username):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''INSERT INTO users (id, username) VALUES (?, ?)''', (user_id, username))
        conn.commit()
        print(f"User {username} added successfully.")
    except sqlite3.IntegrityError:
        print(f"User with id {user_id} already exists.")
    finally:
        conn.close()

# Основная функция
def main():
    # Пример добавления пользователей
    add_user(1, 'User_One')
    add_user(2, 'User_Two')  # Попробуйте добавлять пользователей с разными id

    # Вывод всех пользователей
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    for user in users:
        print(user)

if __name__ == "__main__":
    main()
