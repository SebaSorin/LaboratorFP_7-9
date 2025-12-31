from domain.entities import Reader
from domain.validators import ReaderValidator
import random
import string

class ServiceReader:
    def __init__(self, repo):
        self.__repo = repo

    def add_reader(self, reader_id, reader_name, reader_cnp):
        """
        Adauga la repository un cititor cu datele date
        :param reader_id: id-ul cititorului
        :param reader_name: numele cititorului
        :param reader_cnp: CNP-ul cititorului
        :raises: ValueError daca - deja exista un cititor cu acelasi id
                                 - cititorul nu este valid
        """
        reader = Reader(reader_id, reader_name, reader_cnp)

        validator = ReaderValidator()
        validator.validate(reader)
        self.__repo.add(reader)

    def remove_reader(self, reader_id: int) -> Reader:
        """
        Sterge cititorul din memorie pe baza id-ului
        :param reader_id: id-ul cititorului
        :return: cititorul sters
        :raises: ValueError daca nu exista cititorul dat
        """
        return self.__repo.remove(reader_id)

    def update_reader(self, old_reader_id: int, new_id, new_name, new_cnp) -> Reader:
        """
        Inlocuieste un cititor din memorie cu unul nou
        :param old_reader_id: id-ul cititorului vechi
        :param new_id: id-ul cititorului nou
        :param new_name: numele cititorului nou
        :param new_cnp: cnp-ul cititorului nou
        :return: cititorul inlocuit
        :raises: ValueError daca - nu exista cititor cu id-ul cititorului vechi in memorie
                                 - exista un cititor cu id-ul cititorului nou in memorie
                                 - cititorul nou nu este valid
        """
        new_reader = Reader(new_id, new_name, new_cnp)
        valid = ReaderValidator()
        valid.validate(new_reader)
        return self.__repo.update(old_reader_id, new_reader)

    def get_reader_by_id(self, reader_id: int) -> Reader:
        """
        Returneaza obiectul reader cu id-ul dat
        :param reader_id: id-ul cititorului
        :return: cititorul
        :raises: ValueError daca cititorul nu exista in memorie
        """
        if not reader_id in self.__repo.get_ids():
            raise ValueError("Nu exista cititor cu acest id!")
        result = Reader(1, "", 1)
        for reader in self.__repo.get_readers():
            if reader.get_id() == reader_id:
                result = reader
                break
        return result

    def get_reader_by_id_recursive_version(self, reader_id: int, current_index = 0) -> Reader:
        """
        Returneaza obiectul reader cu id-ul dat
        :param reader_id: id-ul cititorului
        :param current_index: index-ul curent
        :return: cititorul
        :raises: ValueError daca cititorul nu exista in memorie
        """
        if not reader_id in self.__repo.get_ids():
            raise ValueError("Nu exista cititor cu acest id!")

        if self.__repo.get_reader_list()[current_index].get_id() == reader_id:
            return self.__repo.get_reader_list()[current_index]
        return self.get_reader_by_id_recursive_version(reader_id, current_index + 1)



    @staticmethod
    def get_random_reader(sd: int) -> Reader:
        """
        Genereaza o carte cu date random
        :return: cartea generata
        """

        random.seed(sd)
        r_id = random.randint(1, 100000000)
        random.seed(sd)
        r_name = "".join(random.choices(string.ascii_letters, k=10))
        random.seed(sd)
        r_cnp = random.randint(1000000000000, 10000000000000)

        gen_reader = Reader(r_id, r_name, r_cnp)
        return gen_reader







