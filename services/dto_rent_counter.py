


class BookRentCounter:
    def __init__(self, book_instance, book_rent_counter):
        self.__book = book_instance
        self.__counter = book_rent_counter
        if self.__book.get_id() not in self.__counter:
            self.__counter[self.__book.get_id()] = 0

    def get_book(self):
        return self.__book

    def get_counter(self):
        return self.__counter

    def get_times_rented(self):
        return self.__counter[self.__book.get_id()]

    def __str__(self):
        return (f"Cartea {self.__book.get_title()}, scrisa de {self.__book.get_author()} "
                f"a fost inchiriata de {self.__counter[self.__book.get_id()]} ori.")

class ReaderRentCounter:
    def __init__(self, reader_instance, reader_rent_counter):
        self.__reader = reader_instance
        self.__counter = reader_rent_counter
        if self.__reader.get_id() not in self.__counter:
            self.__counter[self.__reader.get_id()] = 0

    def get_reader(self):
        return self.__reader

    def get_counter(self):
        return self.__counter

    def get_times_rented(self):
        return self.__counter[self.__reader.get_id()]

    def __str__(self):
        return (f"Cititorul {self.__reader.get_name()} a inchiriat "
                f"{self.__counter[self.__reader.get_id()]} carti.")
