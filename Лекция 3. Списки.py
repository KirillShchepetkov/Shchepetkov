# Задача №1 по спискам (Раздел: Создание списка и получение элементов)
#
# Создайте список с именем protocols, содержащий 5 строковых элементов —
# названия сетевых протоколов (например, "HTTP", "HTTPS", "FTP", "SSH", "TCP").
#
# Элементы задайте вручную при создании списка.
# Выведите на экран (каждый с новой строки):
# Весь список целиком.
# Первый элемент списка.
# Третий элемент списка.
# Последний элемент списка (используя отрицательный индекс).

#Решение:

protocols = ["HTTP", "HTTPS", "FTP", "SSH", "TCP"]
print(protocols)

first_protocol = protocols[0]
print(first_protocol)

third_protocol = protocols[2]
print(third_protocol)

last_protocol = protocols[-1]
print(last_protocol)

