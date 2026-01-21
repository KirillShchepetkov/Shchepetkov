# Задача №1 (Раздел: Создание строки и базовые методы)
#
# Создайте переменную greeting и присвойте ей строку: " Привет, мир! " (с пробелами в начале и в конце).
# Используя методы строк, выполните последовательно и выведите результат каждого шага (каждый с новой строки):
# Удалите пробелы с обоих концов строки.
# Приведите строку к верхнему регистру.
# Замените слово "мир" на слово "Python".

#Решение

greeting = " Привет, мир! "

trimmed_greeting = greeting.strip()

result = greeting.upper()

new_greeting = greeting.replace("мир", "Python")

print(trimmed_greeting)
print(result)
print(new_greeting)

# Задача №2 (Раздел: Доступ к символам и срезы)
#
# Дана строка:
# text = "автоматизация"
#
# Выведите на экран:
# Первый символ этой строки.
# Последний символ этой строки.
# Символ, который находится ровно посередине строки (7-й символ, считая с 1).
# Используя срезы (slice), выведите на экран:
# Первые 5 символов строки.
# Последние 4 символа строки.
# Каждый второй символ строки, начиная с первого.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 6 строк).

#Решение

text = "автоматизация"

first_char = text[0]
print(first_char)

last_char = text[-1]
print(last_char)

middle_char = text[6]
print(middle_char)

substring1 = text[0:5]
print(substring1)

substring2 = text[-4:]
print(substring2)

substring3 = text[0::2]
print(substring3)

# Задача №3 (Раздел: F-строки и конкатенация)
#
# У вас есть три переменные:
# product = "ноутбук"
# price = 75000
# rating = 4.7
#
# Используя конкатенацию строк (оператор +), создайте строку в формате:
# "Товар: [product], цена: [price] руб."
# и выведите её на экран.
#
# Используя f-строку, создайте строку в формате:
# "Товар: {product}, рейтинг: {rating}"
# и выведите её на экран.
#
# Используя f-строку с выражением, создайте строку в формате:
# "Итого: {цена со скидкой 10%} руб."
# (Рассчитайте цену со скидкой 10% прямо внутри f-строки)
# и выведите её на экран.

product = "ноутбук"
price = 75000
rating = 4.7

price_str = str(price)
greeting = "Товар: " + product + " цена " +price_str+ " руб."
print(greeting)

f_string = f"Товар: {product}, рейтинг: {rating}"
print(f_string)

final_sum = f"Итого:{price*0.9} руб"
print(final_sum)

# Задача №4 (Раздел: Длина строки и срезы)
#
# Дана строка:
# data = "PythonAutomation"
#
# Выведите на экран длину этой строки.
#
# Используя срезы (slice), получите и выведите на экран:
# Подстроку с 3-го по 8-й символ включительно (считая с 1).
# Подстроку, которая состоит из каждого третьего символа, начиная со второго.
# Подстроку, содержащую первые 6 символов.
# Подстроку, содержащую последние 5 символов.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 5 строк).

#Решение:

data = "PythonAutomation"

length = len(data)

substring1 = data[2:8]

substring2 = data[1::3]

substring3 = data[:6]

substring4 = data[-5:]

print(length)
print(substring1)
print(substring2)
print(substring3)
print(substring4)

# Задача №5 (Раздел: Базовые методы строк)
#
# Дана строка:
# log_line = "ERROR: File 'data.txt' not found at 2024-05-15 14:30:00"
#
# Проверьте, начинается ли строка с подстроки "ERROR" (используя метод строк).
# Проверьте, заканчивается ли строка подстрокой "14:30:00" (используя метод строк).
# Найдите и выведите индекс (позицию) первого вхождения подстроки "not" в строке.
# Замените в строке слово "ERROR" на "WARNING".
# Разделите исходную строку на две части по подстроке " at " (с пробелами) и сохраните результат в список. Выведите этот список.
#
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 5 строк).

#Решение

log_line = "ERROR: File 'data.txt' not found at 2024-05-15 14:30:00"

start_result = log_line.startswith("ERROR:")

end_result = log_line.endswith("14:30:00")

log_line1 = log_line.find("not")

new_log_line = log_line.replace("ERROR","WARNING")

parts = log_line.split( " at " )

print(start_result)
print(end_result)
print(log_line1)
print(new_log_line)
print(parts)

# Задача №6 (Раздел: Конкатенация и F-строки)
#
# У вас есть данные:
# user_name = "Алексей"
# completed_tasks = 12
# total_tasks = 15
#
# Используя конкатенацию строк (оператор +), создайте и выведите строку:
# "Пользователь: [user_name]"
#
# Используя f-строку, создайте и выведите строку:
# "Выполнено задач: [completed_tasks] из [total_tasks]"
#
# Используя f-строку с выражением, создайте и выведите строку:
# "Прогресс: [процент выполнения]%"
# (Рассчитайте процент выполнения как (completed_tasks / total_tasks) * 100. Ограничьте вывод до одного знака после запятой, используя форматирование в f-строке: {выражение:.1f}).
#
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 3 строки).

#Решение

user_name = "Алексей"
completed_tasks = 12
total_tasks = 15

string1 = "Пользователь: " + user_name

string2 = f"Выполнено задач: {completed_tasks} из {total_tasks}"

string3  = f"Прогресс: {(completed_tasks / total_tasks) * 100:.1f}%"

print(string1)
print(string2)
print(string3)

# Задача №7 (Раздел: Доступ к символам, срезы, длина)
#
# Дана строка:
# serial_number = "ABC-1234-XYZ"
#
# Выведите на экран:
#
# Длину этой строки.
# Первые 3 символа строки.
# Последние 3 символа строки.
# Используя срезы, получите и выведите:
# Только цифровую часть (цифры между дефисами).
# Символы строки в обратном порядке.
# Используя индексацию, выведите:
# 5-й символ строки (считая с 1).
# 7-й символ строки (считая с 1).
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 7 строк).

#Решение

serial_number = "ABC-1234-XYZ"

length = len(serial_number)

number_3 = serial_number[0:3]

number_3_back = serial_number[-3:]

number_full = serial_number[4:8]

number_back = serial_number[::-1]

symbol_5 = serial_number[4]

symbol_7 = serial_number[6]

print(length)
print(number_3)
print(number_3_back)
print(number_full)
print(number_back)
print(symbol_5)
print(symbol_7)

# Задача №8 (Раздел: Базовые методы строк)
# Дана строка:
# log_message = " WARNING: Disk space is below 15% "
#
# Удалите лишние пробелы с обоих концов строки.
# Проверьте, начинается ли очищенная строка с подстроки "WARNING".
# Найдите и выведите индекс (позицию) подстроки "below" в очищенной строке.
# Замените в очищенной строке "15%" на "10%".
# Приведите очищенную строку к нижнему регистру.
# Выполните все шаги последовательно, используя результат предыдущего шага.
# Выведите на экран результат каждого шага (всего 5 строк).

#Решение

log_message = " WARNING: Disk space is below 15% "

trimmed_log_message = log_message.strip()

start_result = trimmed_log_message.startswith("WARNING")

index_string = trimmed_log_message.find("below")

new_trimmed_log_message = trimmed_log_message.replace("15%", "10%")

down_trimmed_log_message = new_trimmed_log_message .lower()

print(trimmed_log_message)
print(start_result)
print(index_string)
print(new_trimmed_log_message)
print(down_trimmed_log_message)

# Задача №9 (Раздел: F-строки и длина строки)
#
# У вас есть данные:
# project_name = "Autotest_Framework"
# total_modules = 8
# completed_modules = 5
#
# Используя f-строку, создайте и выведите строку:
# "Проект: [project_name]"
#
# Используя f-строку, создайте и выведите строку:
# "Модули: [completed_modules]/[total_modules]"
#
# Используя f-строку с выражением, создайте и выведите строку:
# "Завершено: [процент]%"
#
# (Рассчитайте процент завершения как (completed_modules / total_modules) * 100.
# Ограничьте вывод до целого числа, используя форматирование в f-строке: {выражение:.0f}).
# Выведите длину строки project_name.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 4 строки).

project_name = "Autotest_Framework"
total_modules = 8
completed_modules = 5

project = f"Проект: {project_name}"

modules_info = f"Модули: {completed_modules}/{total_modules}"

procent_final = f"{(completed_modules) / (total_modules) * 100.0:.0f}"

final = f"Завершено: {procent_final}%"

length = len(project_name)

print(project)
print(modules_info)
print(final)
print(length)

# Задача №10 нового цикла (Раздел: Срезы и доступ к символам)
#
# Дана строка:
# invoice = "INV-2024-00789"
#
# Используя индексацию, выведите на экран:
# 1-й символ строки.
# 5-й символ строки (считая с 1).
# 10-й символ строки (считая с 1).
#
# Используя срезы (slice), выведите на экран:
#
# Год (4 цифры после первого дефиса).
# Номер (цифры после второго дефиса).
# Весь номер без дефисов (только цифры).
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 6 строк).

#Решение

invoice = "INV-2024-00789"

invoice_1 = invoice[0]

invoice_2 = invoice[4]

invoice_3 = invoice[9]

year = invoice[4:8]

numb= invoice[9:]

trimmed_invoice = year + numb

print(invoice_1)
print(invoice_2)
print(invoice_3)
print(year)
print(numb)
print(trimmed_invoice)

# Задача №11 нового цикла (Раздел: Базовые методы строк)
#
# Дана строка:
# error_log = "ERROR: User 'admin' not authorized; ERROR: Disk space critical; WARNING: High memory usage"
#
# Проверьте, сколько раз подстрока "ERROR" встречается в строке (используйте метод строк).
# Найдите и выведите индекс (позицию) второго вхождения подстроки "ERROR" в строке.
# Замените все вхождения "ERROR" на "FAIL".
# Разделите исходную строку на отдельные сообщения по разделителю "; " (точка с запятой и пробел). Сохраните результат в список и выведите его.
# Проверьте, содержит ли исходная строка подстроку "WARNING" (используйте метод строк).
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 5 строк).

#Решение

error_log = "ERROR: User 'admin' not authorized; ERROR: Disk space critical; WARNING: High memory usage"

error_log_1 = error_log.count("ERROR")

first_index = error_log.find("ERROR")

second_index = error_log.find("ERROR", first_index + 1)

new_error_log = error_log.replace("ERROR", "FAIL")

messages = error_log.split("; ")

warning_str = error_log.find("WARNING")
has_warning = warning_str != -1

print(error_log_1)
print(first_index)
print(second_index)
print(new_error_log)
print(messages)
print(has_warning)

# Задача №12 нового цикла (Раздел: Конкатенация и F-строки)
#
# У вас есть данные:
# test_case = "Login_Test"
# execution_time = 2.345 (время в секундах)
# status = "PASSED"
#
# Используя конкатенацию строк, создайте и выведите строку:
# "Тест-кейс: [test_case]"
#
# Используя f-строку, создайте и выведите строку:
# "Статус: [status]"
#
# Используя f-строку с форматированием числа, создайте и выведите строку:
# "Время выполнения: [execution_time] сек"
# (Ограничьте вывод времени до двух знаков после запятой, используя форматирование: {переменная:.2f}).
#
# Используя f-строку и все три переменные, создайте одну итоговую строку в формате:
# "[test_case] - [status] за [execution_time с форматированием] секунд"
# и выведите её.
#
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 4 строки).

#Решение:

test_case = "Login_Test"
execution_time = 2.345
status = "PASSED"

string_1 = "Тест-кейс: " + test_case

string_2 = f"Статус: {status}"

string_3 = f"Время выполнения: {execution_time:.2f} сек"

string_4 = f"{test_case} - {status} за {execution_time:.2f} секунд"

print(string_1)
print(string_2)
print(string_3)
print(string_4)

# Задача №13 нового цикла (Раздел: Длина строки, срезы, доступ к символам)
#
# Дана строка:
# api_key = "sk_live_7aB3c9d2E5f4G6h8J0k"
#
# Выведите на экран длину этой строки.
#
# Используя индексацию, выведите на экран:
# 1-й символ.
# 4-й символ (считая с 1).
# 10-й символ (считая с 1).
# Используя срезы (slice), получите и выведите:
# Префикc ключа (первые 7 символов).
# Секретную часть ключа (символы с 8-го до конца).
# Каждый третий символ, начиная со второго.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 7 строк).

#Решение

api_key = "sk_live_7aB3c9d2E5f4G6h8J0k"

length = len(api_key)

index_1 = api_key[0]

index_2 = api_key[3]

index_10 = api_key[9]

index_first_7 = api_key[0:7]

index_secret = api_key[7:]

index_three = api_key[1::3]

print(index_1)
print(index_2)
print(index_10)
print(index_first_7)
print(index_secret)
print(index_three)
print(length)

# Задача №14 нового цикла (Раздел: Базовые методы строк)
#
# Дана строка:
# server_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<!DOCTYPE html><html>"
#
# Проверьте, начинается ли строка с подстроки "HTTP".
# Проверьте, содержит ли строка подстроку "200 OK".
# Найдите и выведите индекс (позицию), где начинается подстрока "<!DOCTYPE".
# Замените в строке "text/html" на "application/json".
# Разделите строку на части по разделителю "\n" (символ переноса строки). Сохраните результат в список и выведите этот список.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 5 строк).

#Решение:

server_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<!DOCTYPE html><html>"

string_HTTP = server_response.startswith("HTTP")

string_200 = server_response.find("200 OK")

string_doctype = server_response.find("<!DOCTYPE")

new_text = server_response.replace("text/html", "application/json")

separate = server_response.split("\n")

print(string_HTTP)
print(string_200 != -1)
print(string_doctype)
print(new_text)
print(separate)

# Задача №15 (Новый раунд: F-строки и длина)
#
# У вас есть данные:
# report_name = "Еженедельный_отчёт"
# total_pages = 42
# current_page = 17
# Используя f-строку, создайте и выведите строку:
# "Отчёт: [report_name]"
# Используя f-строку, создайте и выведите строку:
# "Страница: [current_page] из [total_pages]"
# Выведите длину строки report_name.
# Используя f-строку с выражением, создайте и выведите строку:
# "Прогресс: [процент]%"
# (Рассчитайте процент прочитанного как (current_page / total_pages) * 100. Ограничьте вывод до одного знака после запятой, используя форматирование: {выражение:.1f}).
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 4 строки).

#Решение:

report_name = "Еженедельный_отчёт"
total_pages = 42
current_page = 17

string_1 = f"Отчёт: {report_name}"

string_2 = f"Страница: {current_page} из {total_pages}"

length = len(report_name)

proponent_2 = f"Прогресс: {(current_page / total_pages) * 100:.1f}%"

print(string_1)
print(string_2)
print(length)
print(proponent_2)

# Задача №16 (Новый раунд: Срезы и доступ к символам)
#
# Дана строка:
# transaction_id = "TX-9876-5432-ABCD"
#
# Используя индексацию, выведите на экран:
#
# 1-й символ строки.
# 4-й символ строки (считая с 1).
# 10-й символ строки (считая с 1).
# Используя срезы (slice), выведите на экран:
# Первую группу цифр (4 цифры после первого дефиса).
# Вторую группу цифр (4 цифры после второго дефиса).
# Буквенную часть (символы после третьего дефиса).
# Каждый второй символ строки, начиная с первого.
# Вывод организуйте в столбик (каждый ответ с новой строки, всего 7 строк).

#Решение:

transaction_id = "TX-9876-5432-ABCD"

index_1 = transaction_id[0]

index_2 = transaction_id[3]

index_10 = transaction_id[9]

slice_1 = transaction_id[3:7]

slice_2 = transaction_id[8:12]

book = transaction_id[-4:]

slice_second = transaction_id[::2]

print(index_1)
print(index_2)
print(index_10)
print(slice_1)
print(slice_2)
print(book)
print(slice_second)

# Задача 17 (Новый раунд: Базовые методы строк)
#
# Дана строка:
# log_entry = " [INFO] Connection established with database 'prod_db' at 10:30:15 "
#
# Удалите лишние пробелы с обоих концов строки.
# Проверьте, начинается ли очищенная строка с "[" (открывающей квадратной скобки).
# Найдите и выведите индекс (позицию) подстроки "'prod_db'" (включая одинарные кавычки) в очищенной строке.
# Замените в очищенной строке "prod_db" на "test_db" (обратите внимание: кавычки должны остаться).
# Приведите очищенную строку к нижнему регистру.
# Выполните все шаги последовательно, используя результат предыдущего шага.
# Выведите на экран результат каждого шага (всего 5 строк).

#Решение:

log_entry = " [INFO] Connection established with database 'prod_db' at 10:30:15 "

trimmed = log_entry.strip()

trimmed_start = trimmed.startswith("[")

trimmed_index = trimmed.find("'prod_db'")

trimmed_back = trimmed.replace("prod_db", "test_db")

trimmed_down = trimmed.lower()

print(trimmed)
print(trimmed_start)
print(trimmed_index)
print(trimmed_back)
print(trimmed_down)

# Задача №18 (Новый раунд: Конкатенация и F-строки)
#
# У вас есть данные:
# module = "Авторизация"
# total_tests = 24
# failed_tests = 3
#
# Используя конкатенацию строк, создайте и выведите строку:
# "Модуль: [module]"
#
# Используя f-строку, создайте и выведите строку:
# "Тестов: [total_tests]"
#
# Используя f-строку, создайте и выведите строку:
# "Провалено: [failed_tests]"
#
# Используя f-строку с выражением, создайте и выведите строку:
# "Успешно: [количество]"
# (Рассчитайте количество успешных тестов как total_tests - failed_tests).
#
# Используя f-строку с выражением, создайте и выведите строку:
# "Стабильность: [процент]%"
# (Рассчитайте процент успешных тестов как ((total_tests - failed_tests) / total_tests) * 100.
# Ограничьте вывод до целого числа, используя форматирование: {выражение:.0f}).

#Решение:

module = "Авторизация"
total_tests = 24
failed_tests = 3

module_1 = "Модуль: " + module

test_str = f"Тестов: {total_tests}"

failed_str = f"Провалено: {failed_tests}"

win_str = f"Успешно: {total_tests - failed_tests}"

stab_str = f"Стабильность: {((total_tests - failed_tests) / total_tests) * 100:.0f}%"

print(module_1)
print(test_str)
print(failed_str)
print(win_str)
print(stab_str)

