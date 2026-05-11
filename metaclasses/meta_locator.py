class MetaLocator(type):

   def __new__(cls, name, bases, attrs):
    # Перебираем все атрибуты, переданные в класс
        for key, value in attrs.items():
            if isinstance(value, str):
                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                # Преобразуем строку в локатор, если она начинается с '//'(xPath)
                    attrs[key] = value
        return type.__new__(cls, name, bases, attrs)