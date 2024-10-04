import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('project_freedom.db')
cursor = conn.cursor()

# Функция для добавления данных
def add_user(user_id, username):
    cursor.execute('''
        INSERT INTO users (id, username) VALUES (?, ?)
    ''', (user_id, username))
    conn.commit()
    print(f'User {username} added successfully.')

# Функция для чтения данных
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Пример использования функций
if __name__ == '__main__':
    # Добавление пользователя
    add_user(1, 'User_One')
    
    # Чтение пользователей
    get_users()

# Закрываем соединение с базой данных
conn.close()
