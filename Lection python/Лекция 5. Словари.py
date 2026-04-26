# Задача №1 по словарям (Раздел: Создание словаря и доступ к элементам)
# Вручную создайте словарь с именем user_info, содержащий следующие пары ключ-значение:
#
# Ключ "name" → значение "Анна"
# Ключ "age" → значение 28
# Ключ "city" → значение "Москва"
#
# Выведите на экран (каждое с новой строки):
#
# Весь словарь целиком.
# Значение по ключу "name".
# Значение по ключу "age".

# Решение:
user_info = {

"name" : "Анна",
"age": 28,
"city" : "Москва"

}
print(user_info)
print(user_info["name"])
print(user_info["age"])

# Задача №2 по словарям (Раздел: Добавление и обновление элементов)
#
# У вас есть начальный словарь:
# server_config = {"host": "localhost", "port": 8080}
#
# Добавьте в словарь новый ключ "protocol" со значением "HTTP".
# Обновите значение ключа "port" на "9090" (строку, а не число).
# Добавьте в словарь новый ключ "timeout" со значением 30 (целое число).
# Выведите итоговый словарь на экран.
# Выполните шаги в указанном порядке.

# Решение:
server_config = {"host": "localhost", "port": 8080}

server_config["protocol"] = "HTTP"
server_config["port"] = "9090"
server_config["timeout"] = 30

print(server_config)

# Задача №3 по словарям (Раздел: Удаление элементов словаря)
#
# У вас есть словарь:
# product = {"id": 101, "name": "Ноутбук", "price": 75000, "in_stock": True, "category": "Электроника"}
#
# Удалите из словаря ключ "in_stock" и его значение (используйте метод для удаления по ключу).
# Удалите из словаря ключ "category" и его значение (используйте оператор del).
#
# Выведите на экран:
#
# Итоговый словарь.
# Значение удалённого ключа "in_stock" (сохраните его в переменную при удалении).

# Решение:
product = {"id": 101, "name": "Ноутбук", "price": 75000, "in_stock": True, "category": "Электроника"}

in_stock = product.pop("in_stock")
print(in_stock)

del product ["category"]
print(product)

# Задача №4 по словарям (Раздел: Получение элементов, ключей и значений словаря)
#
# У вас есть словарь:
# employee = {"id": 47, "name": "Игорь", "department": "QA", "salary": 85000}
#
# Получите и выведите на экран (каждое с новой строки):
# Все ключи словаря (в виде списка).
# Все значения словаря (в виде списка).
# Все пары "ключ-значение" (в виде списка кортежей).
# Используя методы словаря, получите и выведите:
# Значение по ключу "department".
# Значение по ключу "name".

# Решение:

employee = {"id": 47, "name": "Игорь", "department": "QA", "salary": 85000}

keys = employee.keys()
print(keys)
values = employee.values()
print(values)
elements = employee.items()
print(elements)

department = employee["department"]
print(department)
name = employee["name"]
print(name)

# Задача №5 по словарям (Раздел: Создание словаря и доступ к элементам)
#
# Вручную создайте словарь с именем test_case, содержащий следующие пары ключ-значение:
# Ключ "id" → значение "TC-001"
# Ключ "title" → значение "Проверка авторизации"
# Ключ "priority" → значение "high"
# Ключ "status" → значение "passed"
#
# Выведите на экран (каждое с новой строки):
#
# Весь словарь целиком.
# Значение по ключу "title".
# Значение по ключу "status".

# Решение:

test_case = {

"id" : "TC-001",
"title" : "Проверка авторизации",
"priority" : "high",
"status" : "passed"
}

print(test_case)
print(test_case["title"])
print(test_case["status"])

# Задача №6 по словарям (Раздел: Добавление и обновление элементов)
#
# У вас есть начальный словарь:
# car = {"brand": "Toyota", "year": 2020}
#
# Добавьте в словарь ключ "model" со значением "Camry".
# Обновите значение ключа "year" на 2022.
# Добавьте в словарь ключ "color" со значением "black".
# Выведите итоговый словарь на экран.
# Выполните шаги в указанном порядке.

# Решение:
car = {"brand": "Toyota", "year": 2020}

car["model"] = "Camry"
car["year"] = 2022
car["color"] = "black"

print(car)

# Задача №7 по словарям (Раздел: Удаление элементов словаря)
#
# У вас есть словарь:
# book = {"title": "Автоматизация тестирования", "author": "Иванов", "pages": 300, "price": 1500, "available": True}
#
# Удалите из словаря ключ "available" и его значение (используйте метод, который возвращает удалённое значение).
# Сохраните удалённое значение в переменную removed_value.
# Удалите из словаря ключ "price" и его значение (используйте оператор del).
# Выведите на экран (каждое с новой строки):
# Итоговый словарь.
# Значение переменной removed_value.

# Решение:
book = {
    "title": "Автоматизация тестирования",
    "author": "Иванов", "pages": 300, "price": 1500, "available": True}

removed_value = book.pop("available")
print(removed_value)

del book["price"]
print(book)

# Задача №8 по словарям (Раздел: Получение элементов, ключей и значений словаря)
#
# У вас есть словарь:
# project = {"name": "Autotest", "language": "Python", "version": 3.9, "active": True}
#
# Получите и выведите на экран (каждое с новой строки):
# Все ключи словаря.
# Все значения словаря.
# Все пары "ключ-значение".
# Используя методы словаря, получите и выведите:
# Значение по ключу "language".
# Значение по ключу "version".

# Решение:
project = {"name": "Autotest", "language": "Python", "version": 3.9, "active": True}

keys = project.keys()
print(keys)
values = project.values()
print(values)
elements = project.items()
print(elements)

language = project["language"]
print(language)
version = project["version"]
print(version)

# Задача №9 по словарям (Раздел: Проверка на наличие ключей и значений)
#
# У вас есть словарь:
# settings = {"theme": "dark", "notifications": True, "language": "ru", "volume": 75}
#
# Проверьте и выведите результат (True или False) для следующих проверок (каждую с новой строки):
# Присутствует ли ключ "notifications" в словаре.
# Присутствует ли ключ "timezone" в словаре.
# Присутствует ли значение "dark" среди значений словаря.
# Присутствует ли значение 100 среди значений словаря.
# Безопасно получите значение по ключу "language"
# (используя метод, который не вызовет ошибку при отсутствии ключа) и сохраните в переменную lang.
# Безопасно получите значение по ключу "font_size" (этого ключа нет в словаре)
# и установите значение по умолчанию 14. Сохраните результат в переменную font.

# Решение:

settings = {"theme": "dark", "notifications": True, "language": "ru", "volume": 75}

print("notifications" in settings)

print("timezone" in settings)

print("dark" in settings)

print("dark" in settings.values())

print(100 in settings.values())

lang  = settings.get("language")
print(lang)
font = settings.get("font_size", 14)
print(font)

# Задача №10 по словарям (Раздел: Создание словаря и доступ к элементам)
#
# Вручную создайте словарь с именем device, содержащий следующие пары ключ-значение:
# Ключ "type" → значение "ноутбук"
# Ключ "os" → значение "Windows 10"
# Ключ "ram_gb" → значение 16
# Ключ "active" → значение True
#
# Выведите на экран (каждое с новой строки):
# Весь словарь целиком.
# Значение по ключу "type".
# Значение по ключу "ram_gb".

# Решение:

device = {
   "type": "ноутбук",
   "os": "Windows 10",
   "ram_gb": 16,
   "active": True
}

print(device)
print(device["type"])
print(device["ram_gb"])