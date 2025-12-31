from domain.entities import Book
from domain.validators import BookValidator
import random
import string

class ServiceBook:
    def __init__(self, repo):
        self.__repo = repo

    def add_book(self, book_id, book_title, book_desc, book_author):
        """
        Adauga la repository o carte cu datele date
        :param book_id: id-ul cartii
        :param book_title: titlul cartii
        :param book_desc: descrierea cartii
        :param book_author: autorul cartii
        :raises: ValueError daca - cartea este invalida
                                 - cartea exista deja in repo
        """
        book = Book(book_id, book_title, book_desc, book_author)
        validator = BookValidator()
        validator.validate(book)
        self.__repo.add(book)

    def remove_book(self, book_id: int) -> Book:
        """
        Sterge cartea cu id-ul dat din memorie
        :param book_id: id-ul cartii
        :return: obiectul carte stearsa
        :raises: ValueError daca cartea nu exista
        """
        return self.__repo.remove(book_id)

    def update_book(self, old_book_id: int, new_id, new_title, new_desc, new_author):
        """
        Inlocuieste o carte din memorie cu una noua
        :param old_book_id: id-ul cartii vechi
        :param new_id: id-ul noii carti
        :param new_title: titlul noii carti
        :param new_desc: descrierea noii carti
        :param new_author: autorul noii carti
        :return: cartea care a fost inlocuita
        :raises: ValueError daca - nu exista carte cu id-ul cartii vechi in memorie
                                 - exista o carte cu id-ul cartii noi in memorie
                                 - cartea noua nu este valida
        """
        new_book = Book(new_id, new_title, new_desc, new_author)
        validator = BookValidator()
        validator.validate(new_book)
        return self.__repo.update(old_book_id, new_book)

    def get_book_by_id(self, book_id: int) -> Book:
        """
        Returneaza obiectul carte cu id-ul dat
        :param book_id: id-ul cartii
        :return: cartea
        :raises: ValueError daca cartea nu exista in memorie
        """
        if not book_id in self.__repo.get_ids():
            raise ValueError("Nu exista carte cu acest id!")
        result = Book(1, "", "", "")
        for book in self.__repo.get_books():
            if book.get_id() == book_id:
                result = book
                break
        return result

    def get_book_by_id_recursive_version(self, book_id: int, current_index = 0) -> Book:
        """
        Returneaza obiectul carte cu id-ul dat
        :param book_id: id-ul cartii
        :param current_index: index-ul curent din lista de carti
        :return: cartea
        :raises: ValueError daca cartea nu exista in memorie
        """
        if not book_id in self.__repo.get_ids() or current_index >= self.__repo.get_size():
            raise ValueError("Nu exista carte cu acest id!")

        if self.__repo.get_book_list()[current_index].get_id() == book_id:
            return self.__repo.get_book_list()[current_index]
        return self.get_book_by_id_recursive_version(book_id, current_index + 1)



    @staticmethod
    def get_random_book(sd: int) -> Book:
        """
        Genereaza o carte cu date random
        :return: cartea generata
        """

        random.seed(sd)
        b_id = random.randint(1, 100000000)
        random.seed(sd)
        b_title = "".join(random.choices(string.ascii_letters, k = 10))
        random.seed(sd+1)
        b_desc = "".join(random.choices(string.ascii_letters, k = 50))
        random.seed(sd+2)
        b_author = "".join(random.choices(string.ascii_letters, k = 10))

        gen_book = Book(b_id, b_title, b_desc, b_author)
        return gen_book






