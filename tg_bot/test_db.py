from database import get_connection, add_product, get_products, delete_product, edit_products, clear_products


def test_database():
    connection = get_connection()
    if not connection:
        return 

    # Добавляем тестовый продукт
    print("Добавляем продукт...")
    add_product("Тестовый продукт", "2024-12-31", 2)    

    # Показываем список до удаления
    print("\nСписок продуктов до удаления:")
    products = get_products()
    for product in products:
        print(product)

    # Удаляем продукт
    print("\nУдаляем продукт...")
    result = delete_product("Тестовый продукт")
    print(f"Результат удаления: {'успешно' if result else 'не найден'}")

    # Показываем список после удаления
    print("\nСписок продуктов после удаления:")
    products = get_products()
    for product in products:
        print(product)


if __name__=="__main__":
    test_database()
    
