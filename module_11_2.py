
def introspection_info(obj):
    """Возвращает словарь с информацией об объекте."""
    # Сбор информации об объекте
    info = {
        'type': str(type(obj)).replace("<class '", "").replace("'>", ""),  # Убираем лишние символы
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],  # Получаем атрибуты
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],  # Фильтруем только методы
        'module': obj.__module__ if hasattr(obj, '__module__') else '__main__',  # Получаем модуль объекта, если он есть
    }

    return info

# Пример использования:
number_info = introspection_info(42)
print('42', number_info)

list_info = introspection_info([1, 2, 3])
print('[1, 2, 3]',list_info)

dict_info = introspection_info({'a': 1, 'b': 2})
print("{'a': 1, 'b': 2}",dict_info)

string_info = introspection_info("Hello")
print('"Hello"',string_info)
