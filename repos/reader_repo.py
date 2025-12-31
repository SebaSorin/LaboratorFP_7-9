from domain.entities import Reader

class RepoReaderMemory:
    def __init__(self):
        # key: id, value = reader instance
        self.__readers = {}

    def get_size(self):
        return len(self.__readers)

    def get_readers(self):
        return self.__readers.values()

    def get_ids(self):
        return self.__readers.keys()

    def get_reader_list(self):
        reader_list = []
        for id in self.get_ids():
            reader_list.append(self.__readers[id])
        return reader_list

    def get_reader_by_id(self, reader_id: int) -> Reader:
        """
        Returneaza cititorul cu id-ul dat
        :param reader_id: id-ul cititorului
        :return: instanta cititor cu id-ul dat
        :raises: ValueError daca id-ul nu apare in memorie
        """
        if reader_id not in self.__readers:
            raise ValueError("Cititorul acesta nu exista in memorie!")
        return self.__readers[reader_id]


    def add(self, reader: Reader) -> None:
        """
        Adauga instanta reader in memorie
        :param reader: obiectul reader
        :return: -; se modifica campul __readers
        :raises: ValueError daca deja exista un cititor cu acelasi id
        """
        if reader.get_id() in self.__readers:
            raise ValueError("Un citior cu acest id exista deja!")
        self.__readers[reader.get_id()] = reader

    def remove(self, reader_id: int) -> Reader:
        """
        Sterge instanta reader din memorie pe baza id-ului si o returneaza
        :param reader_id: id-ul cititorului
        :return: obiectul sters
        :raises: ValueError daca nu exista id-ul in memorie(dictionar)
        """
        if reader_id not in self.__readers:
            raise ValueError("Nu exista cititor cu acest id!")
        deleted_reader = self.__readers[reader_id]
        del self.__readers[reader_id]
        return deleted_reader

    def update(self, old_reader_id: int, new_reader: Reader) -> Reader:
        """
        Inlocuieste o instanta reader cu una noua
        :param old_reader_id: id-ul obiectului reader care va fi inlocuit
        :param new_reader: obiectul reader nou
        :return: obiectul reader inlocuit
        :raises: ValueError daca - nu exista id-ul vechi in memorie(dictionar)
                                 - cititorul nou exista deja in memorie
        """

        if not old_reader_id in self.__readers:
            raise ValueError("Nu exista cititor cu acest id!")

        if new_reader.get_id() in self.__readers:
            raise ValueError("Exista deja un cititor cu acest id!")

        old_reader = self.remove(old_reader_id)
        self.add(new_reader)
        return old_reader


class RepoReaderFile(RepoReaderMemory):
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
            with open(self.__file_name, 'r') as file:
                line_list = file.readlines()
                for line in line_list:
                    line = line.strip()
                    if line:
                        r_id, name, cnp = line.split(',')
                        new_reader = Reader(int(r_id), name, int(cnp))
                        super().add(new_reader)
        except IOError:
            raise IOError("Nu s-au putut citi datele din fisierul " + self.__file_name)

    def __save_to_file(self):
        """
        Salveaza datele din memorie in fisier
        :return: -; se modifica datele din fisierul cu numele self.__file_name
        :raises: IOError daca nu se poate scrie in fisier
        """
        try:
            with open(self.__file_name, 'w') as file:
                readers = super().get_readers()
                for reader in readers:
                    reader_str = (str(reader.get_id()) + ',' +
                                  str(reader.get_name()) + ',' +
                                  str(reader.get_cnp()))
                    reader_str += '\n'
                    file.write(reader_str)
        except IOError:
            raise IOError("Nu s-au putut scrie datele din memorie in fisierul " + self.__file_name)

    def add(self, reader: Reader) -> None:
        super().add(reader)
        self.__save_to_file()

    def remove(self, reader_id: int) -> Reader:
        removed_reader = super().remove(reader_id)
        self.__save_to_file()
        return removed_reader

    def update(self, old_reader_id: int, new_reader: Reader) -> Reader:
        old_reader = super().update(old_reader_id, new_reader)
        self.__save_to_file()
        return old_reader












