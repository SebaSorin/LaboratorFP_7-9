from domain.entities import RentBook, Book, Reader


class RepoRentMemory:
    def __init__(self):
        self.__rentals = []
        #key: book_id, value: times rented
        self.__book_rent_counter = {}
        # key: reader_id, value: times rented
        self.__reader_rent_counter = {}
        self.__rent_history = []

    def get_history(self):
        return self.__rent_history

    def get_size(self):
        return len(self.__rentals)

    def get_rentals(self):
        return self.__rentals

    def get_book_rent_counter(self):
        """
        :return: un dictionar care unde cheile sunt id-urile cartilor
                 iar valorile sunt numarul de ori in care cartea a fost inchiriata
        """
        return self.__book_rent_counter

    def get_reader_rent_counter(self):
        """
            :return: un dictionar care unde cheile sunt id-urile cititorilor
                     iar valorile sunt numarul de inchirieri efectuate de acest cititor
        """
        return self.__reader_rent_counter

    def add(self, rental: RentBook):
        """
        Adauga obiectul inchiriere in memorie
        :param rental: instanta inchiriere
        :raises: ValueError daca cartea este inchiriata deja
        """
        book_in_list = False
        for r in self.__rentals:
            if r.get_book() == rental.get_book():
                book_in_list = True
                break

        if book_in_list:
            raise ValueError("Aceasta carte este deja inchiriata!")
        self.__rentals.append(rental)
        self.__rent_history.append(rental)

        rental_book_id = rental.get_book().get_id()
        if rental_book_id not in self.__book_rent_counter:
            self.__book_rent_counter[rental_book_id] = 0
        self.__book_rent_counter[rental_book_id] += 1

        rental_reader_id = rental.get_reader().get_id()
        if rental_reader_id not in self.__reader_rent_counter:
            self.__reader_rent_counter[rental_reader_id] = 0
        self.__reader_rent_counter[rental_reader_id] += 1

    def find(self, rental: RentBook):
        """
        Cauta in memorie inchirierea data
        :param rental: obiectul inchiriere
        :return: True daca gaseste in memorie o inchiriere pentru
                 aceeasi carte facuta de acelasi cititor
                 False altfel
        """
        return rental in self.__rentals

    def remove(self, rental: RentBook):
        """
        Sterge din memorie inchirierea data
        :param rental: obiectul inchiriere
        :return: inchirierea stearsa
        :raises: ValueError daca nu exista inchirierea in memorie
        """
        if not self.find(rental):
            raise ValueError("Inchirerea aceasta nu exista!")

        del_rental = rental
        for i in range(len(self.__rentals)):
            if self.__rentals[i] == rental:
                del self.__rentals[i]
                break
        return del_rental

class RepoRentFile(RepoRentMemory):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def get_file_name(self):
        return self.__file_name

    def __load_from_file(self):
        """
        Salveaza datele din memorie in fisier
        :return: -; se modifica datele din fisierul cu numele self.__file_name
        :raises: IOError daca nu se poate scrie in fisier
        """
        try:
            with open(self.__file_name, 'r') as file:
                line_list = file.readlines()
                for line in line_list:
                    line = line.strip()
                    if line:
                        book_id, title, description, author, r_id, name, cnp = line.split(',')
                        new_book = Book(int(book_id), title, description, author)
                        new_reader = Reader(int(r_id), name, int(cnp))
                        new_rental = RentBook(new_book, new_reader)
                        super().add(new_rental)
        except IOError:
            raise IOError("Nu s-au putut citi datele din fisierul: " + self.__file_name)

    def __save_to_file(self):
        """
        Salveaza datele din memorie in fisier
        :return: -; se modifica datele din fisierul cu numele self.__file_name
        :raises: IOError daca nu se poate scrie in fisier
        """
        try:
            with open(self.__file_name, 'w') as file:
                rentals = super().get_rentals()
                for rental in rentals:
                    rental_str = (str(rental.get_book().get_id()) + ',' +
                                  str(rental.get_book().get_title()) + ',' +
                                  str(rental.get_book().get_description()) + ',' +
                                  str(rental.get_book().get_author()) + ',' +
                                  str(rental.get_reader().get_id()) + ',' +
                                  str(rental.get_reader().get_name()) + ',' +
                                  str(rental.get_reader().get_cnp()))
                    rental_str += '\n'
                    file.write(rental_str)
        except IOError:
            raise IOError("Nu s-au putut salva datele din memorie in fisierul " + self.__file_name)

    def add(self, rental: RentBook):
        super().add(rental)
        self.__save_to_file()

    def remove(self, rental: RentBook):
        removed_rental = super().remove(rental)
        self.__save_to_file()
        return removed_rental






                





