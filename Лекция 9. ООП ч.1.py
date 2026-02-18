# Задача №1 по ООП (Раздел: Создание класса, объект класса)
#
# Создайте класс Browser.
#
# Внутри класса создайте метод __init__, который:
# Принимает параметры self, name и version.
# Сохраняет name и version как атрибуты экземпляра (self.name = name, self.version = version).
# Создайте два объекта класса Browser:
# Первый объект с именем "Chrome" и версией "120.0"
# Второй объект с именем "Firefox" и версией "115.0"
# Выведите на экран (каждое с новой строки):
# Имя и версию первого браузера в формате: "Браузер: Chrome, версия: 120.0"
# Имя и версию второго браузера в том же формате.
# Используйте обращения к атрибутам объекта (например, browser1.name).

# Решение:

class Browser:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def display(self):
        print(f"Браузер: {self.name}, версия: {self.version}")

Browser_Chrome = Browser("Chrome", 120.0)

Browser_Firefox = Browser("Firefox", 115.0)

Browser_Chrome.display()
Browser_Firefox.display()


# Задача №2 по ООП (Раздел: Общие атрибуты)
#
# Создайте класс Employee.
#
# Добавьте в класс общий атрибут company со значением "TechCorp".
# Создайте конструктор __init__, который принимает параметры self, name и position и
# сохраняет их как атрибуты экземпляра.
#
# Создайте метод info, который выводит на экран:
# "{name} работает в компании {company} на должности {position}"
# Создайте два объекта класса Employee:
# "Анна", должность "тестировщик"
# "Борис", должность "разработчик"
#
# Для каждого объекта вызовите метод info.
# Обратите внимание: Общий атрибут company должен быть доступен внутри метода
# через self.company или Employee.company.

# Решение:

class Employee:
    company = "TechCorp"

    def __init__(self, name,  position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"{self.name} работает в компании {self.company} на должности {self.position}")

Employee_1 = Employee("Анна", "тестировщик")
Employee_2 = Employee("Борис", "разработчик")

Employee_1.display_info()
Employee_2.display_info()

# Задача №3 по ООП (Раздел: Конструктор класса init и методы)
#
# Создайте класс TestResult.
# В конструкторе __init__ определите следующие атрибуты:
#
# test_name — название теста
# status — статус ("passed" или "failed")
# execution_time — время выполнения (число)
#
# Создайте метод display, который выводит информацию о тесте в формате:
# "Тест: {test_name}, статус: {status}, время: {execution_time} сек"
# Создайте метод is_passed, который возвращает True, если статус теста "passed", и False в противном случае.
# Создайте три объекта класса TestResult с разными данными.
# Для каждого объекта:
# Вызовите метод display.
# Вызовите метод is_passed и выведите результат (True/False) на экран.
# Каждая пара (display и is_passed) должна выводиться с новой строки.

# Решение:

class TestResult:
    def __init__(self, test_name, status, execution_time):
        self.test_name = test_name
        self.status = status
        self.execution_time = execution_time

    def display_info(self):
        print(f"Тест: {self.test_name}, статус: {self.status}, время: {self.execution_time} сек")

    def is_passed (self):
        return self.status == "passed"

test1 = TestResult("Авторизация", "passed", 2.5)
test2 = TestResult("Регистрация", "failed", 3.2)
test3 = TestResult("Поиск", "passed", 1.8)

test1.display_info()
print(test1.is_passed())

test2.display_info()
print(test2.is_passed())

test3.display_info()
print(test3.is_passed())




