class BookValidator:
    @staticmethod
    def validate(book):
        """
        Valideaza datele cartii date
        title, description = sir de caratere nevid
        author = sir de caratere nevid fara cifre
        :param book: obiectul Book
        :return: -; afiseaza greselile de introducere a datelor
        """
        errors = []

        if book.get_id() == "":
            errors.append("Id-ul nu poate fi vid.")
        if book.get_title() == "":
            errors.append("Titlul nu poate fi vid.")
        if book.get_description() == "":
            errors.append("Descrierea nu poate fi vida.")
        if book.get_author() == "":
            errors.append("Numele autorului nu poate fi vid.")

        if len(errors) > 0:
            raise ValueError('\n'.join(errors))



class ReaderValidator:
    @staticmethod
    def validate(reader):
        """
        Valideaza datele citiorului dat
        name = sir de caratere nevid
        cnp = numar natural de 13 cifre
        :param reader: obiectul Reader
        :return: -; afiseaza greselile de introducere a datelor
        """
        errors = []

        if reader.get_id() == "":
            errors.append("Id-ul nu poate fi vid.")
        if reader.get_name() == "":
            errors.append("Numele nu poate fi vid.")
        if reader.get_cnp() == "":
            errors.append("CNP-ul nu poate fi vid.")

        if type(reader.get_cnp()) != int:
            errors.append("CNP-ul trebuie sa contina doar cifre!")

        digit_count = 0
        cnp_copy = reader.get_cnp()
        while cnp_copy > 0:
            cnp_copy //= 10
            digit_count += 1

        if digit_count != 13:
            errors.append("CNP-ul trebuie sa aiba 13 cifre!")


        if len(errors) > 0:
            raise ValueError('\n'.join(errors))










