import mysql.connector
from config import DB_CONFIG


def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к базе данных: {err}")    
        return None

def add_product(name, expiration_date=None, quantity=1):
    connection = get_connection()        
    if not connection:
        return False

    cursor = connection.cursor()    
    try:
        query = """
        INSERT INTO products (name, expiration_date, quantity)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, expiration_date, quantity))
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Ошибка при добавлении продукта: {err}")
        return False
    finally:
        cursor.close()
        connection.close()    


def get_products():
    connection = get_connection()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Ошибка при получении списка продуктов: {err}")
        return []
    finally:
        cursor.close()
        connection.close()             


def delete_product(name):
    connection = get_connection()
    if not connection:
        return False

    cursor = connection.cursor()
    try:
        query = "DELETE FROM products WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Ошибка при удалении продукта: {err}")
        return False
    finally:
        cursor.close()
        connection.close()        


def clear_products():
    connection = get_connection()
    if not connection:
        return False

    cursor = connection.cursor()
    try:
        cursor.execute("TRUNCATE TABLE products")
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Ошибка при очистки таблицы: {err}")
        return False
    finally:
        cursor.close()
        connection.close()


def edit_products(name, new_expiration_date=None, new_quantity=None):
    connection = get_connection()
    if not connection:
        return False

    cursor = connection.cursor()
    try:
        updates = []
        values = []
        if new_expiration_date:
            updates.append("expiration_date = %s")
            values.append(new_expiration_date)
        if new_quantity:
            updates.append("quantity = %s")    
            values.append(new_quantity)

        if not updates:
            return False

        query = f"UPDATE products SET {', '.join(updates)} WHERE name = %s"
        values.append(name)
        
        cursor.execute(query, tuple(values))
        connection.commit()
        return cursor.rowcount > 0
    except mysql.connector.Error as err:
        print(f"Ошибка при обновлении продукта: {err}")
        return False
    finally:
        cursor.close()
        connection.close()