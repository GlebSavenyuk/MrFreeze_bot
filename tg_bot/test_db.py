from database import get_connection, add_product, get_products, delete_product, edit_products, clear_products


def test_database():
    connection = get_connection()
    if not connection:
        return 

    # Очищаем таблицу перед тестами
    print("Очищаем таблицу...")
    clear_products()

    # Тест добавления продуктов
    print("\nДобавляем продукты...")
    add_product("Молоко", "2024-02-10", 2)
    add_product("Хлеб", "2024-02-01", 1)
    add_product("Сыр", "2024-03-15", 3)

    # Показываем список продуктов
    print("\nСписок всех продуктов:")
    products = get_products()
    for product in products:
        print(product)

    # Тест редактирования продукта
    print("\nРедактируем количество молока...")
    result = edit_products("Молоко", new_quantity=5)
    print(f"Результат редактирования: {'успешно' if result else 'не удалось'}")

    # Проверяем изменения
    print("\nСписок после редактирования:")
    products = get_products()
    for product in products:
        print(product)

    # Тест удаления продукта
    print("\nУдаляем хлеб...")
    result = delete_product("Хлеб")
    print(f"Результат удаления: {'успешно' if result else 'не удалось'}")

    # Финальная проверка
    print("\nФинальный список продуктов:")
    products = get_products()
    for product in products:
        print(product)

    # Очищаем таблицу
    print("\nОчищаем таблицу...")
    clear_products()
    
    print("\nПроверяем, что таблица пуста:")
    products = get_products()
    if not products:
        print("Таблица успешно очищена")
    else:
        print("Ошибка: таблица не пуста")


if __name__=="__main__":
    test_database()
    
