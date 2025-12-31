from domain.entities import RentBook
from services.dto_rent_counter import BookRentCounter, ReaderRentCounter

class ServiceRent:
    def __init__(self, rent_repo, book_repo, reader_repo):
        self.__rent_repo = rent_repo
        self.__book_repo = book_repo
        self.__reader_repo = reader_repo

    def get_repo_rentals(self):
        return self.__rent_repo.get_rentals()

    def rent_book(self, book_id: int, reader_id: int):
        """
        Adauga o inchiriere la memorie
        :param book_id: id-ul cartii care va fi inchiriata
        :param reader_id: id-ul cititorului care va inchiria cartea
        :raises: ValueError daca - cartea nu apare in memorie
                                 - cititorul nu apare in memorie
                                 - cartea este deja inchiriata
        """

        if book_id not in self.__book_repo.get_ids():
            raise ValueError("Cartea aceasta nu exista in memorie!")

        if reader_id not in self.__reader_repo.get_ids():
            raise ValueError("Cititorul acesta nu exista in memorie!")

        rental = RentBook(self.__book_repo.get_book_by_id_recursive_version(book_id),
                          self.__reader_repo.get_reader_by_id_recursive_version(reader_id))
        self.__rent_repo.add(rental)

    def return_book(self, book_id: int, reader_id: int):
        """
        Se face inapoierea unei carti inchiriate
        :param book_id: id-ul cartii inchiriate
        :param reader_id: id-ul cititorul care a inchiriat cartea
        :returns: instanta inchiriere stearsa
        :raises: ValueError daca - id-ul de carte este invalid
                                 - id-ul de cititor este invalid
                                 - nu exista inchierea in memorie
        """
        if book_id not in self.__book_repo.get_ids():
            raise ValueError("Cartea aceasta nu exista in memorie!")

        if reader_id not in self.__reader_repo.get_ids():
            raise ValueError("Cititorul acesta nu exista in memorie!")

        rental = RentBook(self.__book_repo.get_book_by_id_recursive_version(book_id),
                          self.__reader_repo.get_reader_by_id_recursive_version(reader_id))
        return self.__rent_repo.remove(rental)

    def get_most_rented_books_list(self, n = 3):
        """
        Returneaza o lista cu informatii despre cele mai inchiriate n carti
        :return: lista de DTO's care o sa contina - instanta carte
                                                  - numarul de inchirieri
        :raises: ValueError daca sunt mai putin de n carti
        """
        if len(self.__book_repo.get_ids()) < n:
            raise ValueError("Nu exista destule carti pentru acest raport")

        dto_dict = {}
        for book in self.__book_repo.get_books():
            dto_book = BookRentCounter(book, self.__rent_repo.get_book_rent_counter())
            dto_dict[book.get_id()] = dto_book

        dto_list = list(dto_dict.values())
        dto_list = sorted(dto_list, key=lambda dto: dto.get_times_rented(), reverse=True)
        dto_list = dto_list[:n]
        return dto_list

    def get_most_rented_readers_list(self, n = 3):
        """
        Returneaza o lista cu informatii despre cititorii cu cele mai multe carti inchiriate
        :return: lista de DTO's care o sa contina - instanta cititor
                                                  - numarul de inchirieri
        :raises: ValueError daca sunt mai putin de n cititori
        """
        if len(self.__reader_repo.get_ids()) < n:
            raise ValueError("Nu exista destui cititori pentru acest raport")

        dto_dict = {}
        for reader in self.__reader_repo.get_readers():
            dto_reader = ReaderRentCounter(reader, self.__rent_repo.get_reader_rent_counter())
            dto_dict[reader.get_id()] = dto_reader

        dto_list = list(dto_dict.values())
        dto_list = sorted(dto_list, key=lambda dto: dto.get_times_rented(), reverse=True)
        dto_list = dto_list[:n]
        return dto_list

    def get_most_rented_books_by_most_rented_readers(self, n = 3):
        """
        Returneaza o lista cu informatii despre cele mai inchiriate n carti
        care au fost inchiriate de cei mai acitivi n cititori
        :return: un dictionar cu DTO's de forma - key: id-ul cartii
                                                - value: instanta cititor
        :raises: ValueError daca sunt mai putin de n - carti
                                                     - cititori
        """
        if len(self.__book_repo.get_ids()) < n:
            raise ValueError("Nu exista destule carti pentru acest raport")

        if len(self.__reader_repo.get_ids()) < n:
            raise ValueError("Nu exista destui cititori pentru acest raport")

        dto_dict = {}
        dto_book_list = self.get_most_rented_books_list()
        dto_reader_list = self.get_most_rented_readers_list()
        for i in range(n):
            rental = RentBook(dto_book_list[i].get_book(), dto_reader_list[i].get_reader())
            if (rental in self.__rent_repo.get_history() and
                self.__rent_repo.get_book_rent_counter()[rental.get_book().get_id()] ==
                self.__rent_repo.get_reader_rent_counter()[rental.get_reader().get_id()]):
                dto_dict[dto_book_list[i].get_book().get_id()] = dto_reader_list[i].get_reader()

        return dto_dict






