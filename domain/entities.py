class Book:
    def __init__(self, id: int, title: str, description: str, author: str):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_author(self):
        return self.__author

    def set_title(self, new_title):
        self.__title = new_title

    def set_description(self, new_description):
        self.__description = new_description

    def set_author(self, new_author):
        self.__author = new_author

    def __str__(self):
        return f"Carte #{self.__id} titlu: {self.__title}, autor: {self.__author}, descriere:\n{self.__description}."

    def __eq__(self, other):
        return (self.get_id() == other.get_id() and
                self.get_title() == other.get_title() and
                self.get_author() == other.get_author() and
                self.get_description() == other.get_description())


class Reader:
    def __init__(self, id: int, name: str, cnp: int):
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def set_name(self, new_name):
        self.__name = new_name

    def set_cnp(self, new_cnp):
        self.__cnp = new_cnp

    def __str__(self):
        return f"Cititor #{self.__id}, nume: {self.__name}, CNP: {self.__cnp}"

    def __eq__(self, other):
        return (self.get_id() == other.get_id() and
                self.get_name() == other.get_name() and
                self.get_cnp() == other.get_cnp())


class RentBook:
    def __init__(self, r_book, r_reader):
        self.__book = r_book
        self.__reader = r_reader

    def get_book(self):
        return self.__book

    def get_reader(self):
        return self.__reader

    def set_book(self, new_book):
        self.__book = new_book

    def set_reader(self, new_reader):
        self.__reader = new_reader

    def __str__(self):
        return (f"Cartea {self.__book.get_title()} (id: {self.__book.get_id()})"
                f" a fost inchiriata de {self.__reader.get_name()} (id: {self.__reader.get_id()}).")

    def __eq__(self, other):
        return (self.__book == other.__book and
                self.__reader == other.__reader)










