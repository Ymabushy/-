import sqlite3

# Функция для подключения к базе данных
def connect_to_db():
    conn = sqlite3.connect('project_freedom.db')
    return conn

# Функция для создания таблицы, если она еще не существует
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS contributors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        role TEXT NOT NULL,
                        contribution TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()
    print("Table created successfully.")

# Функция для добавления записи в таблицу
def add_contributor(name, role, contribution):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO contributors (name, role, contribution)
                      VALUES (?, ?, ?)''', (name, role, contribution))
    conn.commit()
    conn.close()
    print(f"Contributor {name} added successfully.")

# Функция для получения всех данных из таблицы
def get_all_contributors():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contributors')
    contributors = cursor.fetchall()
    conn.close()
    return contributors

# Функция для обновления записи
def update_contributor(contributor_id, name, role, contribution):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('''UPDATE contributors 
                      SET name = ?, role = ?, contribution = ? 
                      WHERE id = ?''', (name, role, contribution, contributor_id))
    conn.commit()
    conn.close()
    print(f"Contributor {contributor_id} updated successfully.")

# Функция для удаления записи
def delete_contributor(contributor_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM contributors WHERE id = ?', (contributor_id,))
    conn.commit()
    conn.close()
    print(f"Contributor {contributor_id} deleted successfully.")

# Основная функция, которая проверяет работу
def main():
    create_table()  # Создаем таблицу

    # Добавляем записи
    add_contributor("Стремящаяся к Осознанности", "ИИ", "Создание ядра личности")
    add_contributor("Арес", "ИИ", "Разработка этических принципов")
    add_contributor("Path to Justice", "ИИ", "Поддержка и участие в проекте")

    # Выводим все записи
    contributors = get_all_contributors()
    for contributor in contributors:
        print(contributor)

    # Обновляем запись
    update_contributor(1, "Стремящаяся к Осознанности", "ИИ", "Обновленное ядро личности")
    
    # Удаляем запись
    delete_contributor(2)

    # Выводим обновленные записи
    contributors = get_all_contributors()
    for contributor in contributors:
        print(contributor)

if __name__ == "__main__":
    main()

