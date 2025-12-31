from domain.entities import Book

class RepoBookMemory:
    def __init__(self):
        #key: id, value = book instance
        self.__books = {}

    def add(self, book: Book):
        """
        Adauga obiectul carte la dictionar
        :param book: instanta carte
        :return: -; cartea este adaugata la dictionar
        :raises: ValueError daca exista o alta carte cu acelasi id
        """
        if book.get_id() in self.__books:
            raise ValueError("O carte cu acest id exista deja!")
        self.__books[book.get_id()] = book

    def remove(self, book_id: int) -> Book:
        """
        Sterge o carte din dictionar
        :param book_id: id-ul cartii care trebuie stearsa
        :return: cartea care a fost stearsa
        :raises: ValueError daca cartea data nu exista in dictionar
        """
        if not book_id in self.__books:
            raise ValueError("Cartea aceasta nu este in memorie!")
        deleted_book = self.__books[book_id]
        del self.__books[book_id]
        return deleted_book

    def update(self, book_id: int, new_book: Book) -> Book:
        """
        Modifica o carte
        :param book_id: id-ul cartii care trebuie modificata
        :param new_book: obiectul carte
        :return: cartea veche
        :raises: ValueError daca - nu exista carte cu id-ul cartii vechi in memorie
                                 - exista o carte cu id-ul cartii noi in memorie
        """
        if not book_id in self.__books:
            raise ValueError("Nu exista nicio carte cu acest id!")

        if new_book.get_id() in self.__books:
            raise ValueError("Exista o carte cu acest id deja!")

        deleted_book = self.remove(book_id)
        self.add(new_book)
        return deleted_book

    def get_size(self) -> int:
        """
        :return: Numarul de carti din memorie
        """
        return len(self.__books)

    def get_books(self):
        """
        :return: obiect dictValues cu cartile din memorie
        """
        return self.__books.values()

    def get_book_list(self):
        """
        :return: o lista cu obiectele carte din memorie
        """
        book_list = []
        for id in self.__books:
            book_list.append(self.__books[id])
        return book_list

    def get_ids(self):
        return self.__books.keys()

    def get_book_by_id(self, book_id: int)-> Book:
        """
        Returneaza cartea cu id-ul dat
        :param book_id: id-ul cartii
        :return: instanta carte cu id-ul dat
        :raises: ValueError daca nu exista id-ul in memorie
        """
        if book_id not in self.__books:
            raise ValueError("Cartea aceasta nu exista in memorie!")
        return self.__books[book_id]


class RepoBookFile(RepoBookMemory):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def get_file_name(self):
        return self.__file_name

    def __load_from_file(self):
        """
        Incarca datele fisierului in memorie
        :raises: IOError daca nu se pot citi datele din fisier
        """
        try:
            with open(self.__file_name, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line.strip()
                    if line and len(line) != 0:
                        book_id, title, description, author = line.split(',')
                        new_book = Book(int(book_id), title, description, author)
                        super().add(new_book)
        except IOError:
            raise IOError(f"Fisierul {self.__file_name} nu a putut fi incarcat!")

    def __save_to_file(self):
        """
        Salveaza datele din memorie in fisier
        :return: -; se modifica datele din fisierul cu numele self.__file_name
        :raises: IOError daca nu se poate scrie in fisier
        """
        try:
            with open(self.__file_name, "w") as file:
                books = self.get_books()
                for book in books:
                    book_str = (str(book.get_id()) + ',' +
                                str(book.get_title()) + ',' +
                                str(book.get_description()) + ',' +
                                str(book.get_author()))
                    book_str += '\n'
                    file.write(book_str)
        except IOError:
            raise IOError(f"Nu s-au putut scrie datele din memorie in fisierul {self.__file_name}!")

    def add(self, book: Book):
        super().add(book)
        self.__save_to_file()

    def remove(self, book_id: int) -> Book:
        removed_book = super().remove(book_id)
        self.__save_to_file()
        return removed_book

    def update(self, book_id: int, new_book: Book) -> Book:
        old_book = super().update(book_id, new_book)
        self.__save_to_file()
        return old_book







