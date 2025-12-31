import random

class Console:
    def __init__(self, book_service, reader_service, rent_service):
        self.__book_service = book_service
        self.__reader_service = reader_service
        self.__rent_service = rent_service

    @staticmethod
    def print_memory_type():
        print("Alegeti tipul de memorie:")
        print("F.Fisiere")
        print("T.Temporara")

    @staticmethod
    def print_menu():
        print("Comenzi:")
        print("1.Adauga")
        print("2.Sterge dupa id")
        print("3.Modifica")
        print("4.Inchiriaza carte")
        print("5.Returneaza carte")
        print("---" * 10)
        print("C.Cauta dupa id")
        print("G.Genereaza")
        print("R.Raport")
        print("E.Exit")

    @staticmethod
    def print_type_menu():
        print("Tipul:")
        print("B.Carte")
        print("R.Cititor")

    @staticmethod
    def print_stats_menu():
        print("Tipul:")
        print("A.Cele mai inchiriate carti")
        print("B.Toate cartile inchiriate de cititori")
        print("C.Cei mai activi cititori")
        print("D.Cei mai activi cititori cu cele mai inchiriate carti")

#-------------------book methods---------------------
    def __add_book_ui(self):
        c_id = input("Id carte: ")
        c_title = input("Titlu carte: ")
        c_desc = input("Descriere carte: ")
        c_author = input("Autor carte: ")

        try:
            c_id = int(c_id)
            self.__book_service.add_book(c_id, c_title, c_desc, c_author)
        except ValueError as e:
            print(str(e))
        else:
            print("Cartea a fost adaugata cu succes!")

    def __remove_book_ui(self):
        c_id = input("Id carte: ")

        try:
            c_id = int(c_id)
            removed_book = self.__book_service.remove_book(c_id)
        except ValueError as e:
            print(str(e))
        else:
            print(f"Cartea {removed_book} a fost stearsa cu succes!")

    def __update_book_ui(self):
        old_id = input("Id carte inlocuita: ")
        new_id = input("Id nou: ")
        new_title = input("Titlu nou: ")
        new_desc = input("Descriere noua: ")
        new_author = input("Autor nou: ")

        try:
            old_id = int(old_id)
            new_id = int(new_id)
            old_book = self.__book_service.update_book(old_id, new_id, new_title, new_desc, new_author)
        except ValueError as e:
            print(str(e))
        else:
            print(f"Cartea {old_book} a fost modificata cu succes!")

    def __search_book_ui(self):
        b_id = input("Id carte: ")

        try:
            b_id = int(b_id)
            found_book = self.__book_service.get_book_by_id_recursive_version(b_id)
            print(found_book)
        except ValueError as e:
            print(str(e))

    def __generate_book_ui(self):
        sd = random.randint(1, 10000)
        gen_book = self.__book_service.get_random_book(sd)
        print(gen_book)


#-------------------reader methods---------------------
    def __add_reader_ui(self):
        r_id = input("Id cititor: ")
        r_name = input("Nume cititor: ")
        r_cnp = input("CNP cititor: ")

        try:
            r_id = int(r_id)
            r_cnp = int(r_cnp)
            self.__reader_service.add_reader(r_id, r_name, r_cnp)
        except ValueError as e:
            print(str(e))
        else:
            print("Cititorul a fost adaugat cu succes!")

    def __remove_reader_ui(self):
        r_id = input("Id cititor: ")

        try:
            r_id = int(r_id)
            removed_reader = self.__reader_service.remove_reader(r_id)
        except ValueError as e:
            print(str(e))
        else:
            print(f"Cititorul {removed_reader} a fost sters cu succes!")

    def __update_reader_ui(self):
        old_id = input("Id cititor inlocuit: ")
        new_id = input("Id nou: ")
        new_name = input("Nume nou: ")
        new_cnp = input("CNP nou: ")

        try:
            old_id = int(old_id)
            new_id = int(new_id)
            new_cnp = int(new_cnp)
            old_reader = self.__reader_service.update_reader(old_id, new_id, new_name, new_cnp)
        except ValueError as e:
            print(str(e))
        else:
            print(f"Cititorul {old_reader} a fost modificat cu succes!")

    def __search_reader_ui(self):
        r_id = input("Id cititor: ")

        try:
            r_id = int(r_id)
            found_reader = self.__reader_service.get_reader_by_id_recursive_version(r_id)
            print(found_reader)
        except ValueError as e:
            print(str(e))

    def __generate_reader_ui(self):
        sd = random.randint(1, 10000)
        gen_reader = self.__reader_service.get_random_reader(sd)
        print(gen_reader)

# -------------------rent methods---------------------
    def __rent_book_ui(self):
        book_id = input("Id carte: ")
        reader_id = input("Id cititor: ")

        try:
            book_id = int(book_id)
            reader_id = int(reader_id)
            self.__rent_service.rent_book(book_id, reader_id)
            print("Inchiriere efectuata!")
        except ValueError as e:
            print(str(e))

    def __return_book_ui(self):
        book_id = input("Id carte: ")
        reader_id = input("Id cititor: ")

        try:
            book_id = int(book_id)
            reader_id = int(reader_id)
            self.__rent_service.return_book(book_id, reader_id)
            print("Returnare efectuata!")
        except ValueError as e:
            print(str(e))

#-------------------stats methods---------------------
    def __most_rented_book_ui(self):
        try:
            dto_list = self.__rent_service.get_most_rented_books_list()
            for dto in dto_list:
                print(dto)
        except ValueError as e:
            print(str(e))

    def __most_rented_reader_ui(self):
        try:
            dto_list = self.__rent_service.get_most_rented_readers_list()
            for dto in dto_list:
                print(dto)
        except ValueError as e:
            print(str(e))

    def __most_rented_book_by_most_rented_reader_ui(self):
        try:
            result_dict = self.__rent_service.get_most_rented_books_by_most_rented_readers()
            if len(result_dict) == 0:
                print("Nu exista cititori care sa indeplineasca conditia!")
            for book_id in result_dict:
                print(f"Cititorul {result_dict[book_id].get_id()} a inchiriat "
                      f"cartea {self.__book_service.get_book_by_id_recursive_version(book_id).get_title()}")
        except ValueError as e:
            print(str(e))

    def __print_rented_books_ui(self):
        rental_list = self.__rent_service.get_repo_rentals()
        if len(rental_list) == 0:
            print("Nu exista inchirieri in memorie!")
        else:
            for rental in rental_list:
                print(rental)

    def run(self):
        # functia principala

        while True:
            self.print_menu()
            option = input(">>>").strip()
            if option == "1":
                self.print_type_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "B":
                    self.__add_book_ui()
                elif option_type.upper() == "R":
                    self.__add_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option == "2":
                self.print_type_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "B":
                    self.__remove_book_ui()
                elif option_type.upper() == "R":
                    self.__remove_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option == "3":
                self.print_type_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "B":
                    self.__update_book_ui()
                elif option_type.upper() == "R":
                    self.__update_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option == "4":
                self.__rent_book_ui()
            elif option == "5":
                self.__return_book_ui()
            elif option.upper() == "C":
                self.print_type_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "B":
                    self.__search_book_ui()
                elif option_type.upper() == "R":
                    self.__search_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option.upper() == "G":
                self.print_type_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "B":
                    self.__generate_book_ui()
                elif option_type.upper() == "R":
                    self.__generate_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option.upper() == "R":
                self.print_stats_menu()
                option_type = input(">>>").strip()

                if option_type.upper() == "A":
                    self.__most_rented_book_ui()
                elif option_type.upper() == "B":
                    self.__print_rented_books_ui()
                elif option_type.upper() == "C":
                    self.__most_rented_reader_ui()
                elif option_type.upper() == "D":
                    self.__most_rented_book_by_most_rented_reader_ui()
                else:
                    print("Comanda invalida!")
            elif option.upper() == "E":
                break
            else:
                print("Comanda invalida!")









