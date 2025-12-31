from domain.entities import Book
from services.book_service import ServiceBook
from repos.book_repo import RepoBookMemory


def test_book_service_add_book():
    test_repo = RepoBookMemory()
    test_service = ServiceBook(test_repo)

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    assert test_repo.get_size() == 1
    assert book1 in test_repo.get_books()

    test_service.add_book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    assert test_repo.get_size() == 2
    assert book2 in test_repo.get_books()

    #carte existenta
    try:
        test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        assert False
    except ValueError:
        assert True

    #carte invalida
    try:
        test_service.add_book(3, "", "", "")
        assert False
    except ValueError:
        assert True

def test_book_service_remove_book():
    test_repo = RepoBookMemory()
    test_service = ServiceBook(test_repo)

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

    test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    del_book = test_service.remove_book(1)
    assert test_repo.get_size() == 0
    assert not book1 in test_repo.get_books()
    assert book1 == del_book

    #carte non-existenta
    try:
        test_service.remove_book(2)
        assert False
    except ValueError:
        assert True

def test_book_service_update_book():
    test_repo = RepoBookMemory()
    test_service = ServiceBook(test_repo)

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    old_book = test_service.update_book(1, 2, "The Hobbit", "Roman fantasy", "Tolkien")
    assert old_book == book1
    assert book2 in test_repo.get_books()
    assert test_repo.get_size() == 1

    #id gresit
    try:
        test_service.update_book(50, 1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        assert False
    except ValueError:
        assert True

    #id nou existent
    try:
        test_service.update_book(2, 2, "Atomic Habits", "Carte self-help", "James Clear")
        assert False
    except ValueError:
        assert True

    #carte noua invalida
    try:
        test_service.update_book(2, 0, "", "", "")
        assert False
    except ValueError:
        assert True

def test_book_service_generate_book():
    test_repo = RepoBookMemory()
    test_service = ServiceBook(test_repo)

    gen_book = test_service.get_random_book(1)
    assert gen_book == test_service.get_random_book(1)

    gen_book = test_service.get_random_book(45)
    assert gen_book == test_service.get_random_book(45)

    gen_book = test_service.get_random_book(10000)
    assert gen_book == test_service.get_random_book(10000)


"""if __name__ == "__main__":
    test_book_service_add_book()
    test_book_service_remove_book()
    test_book_service_update_book()
    test_book_service_generate_book()"""

import unittest

class TestCaseBookServiceMemory(unittest.TestCase):
    def setUp(self):
        self.__test_repo = RepoBookMemory()
        self.__test_service = ServiceBook(self.__test_repo)
        self.__book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

    def tearDown(self):
        del self.__test_repo
        del self.__test_service
        del self.__book

    def test_add_book(self):
        # caz general
        self.__test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        self.assertTrue(self.__book in self.__test_repo.get_books())

        # carte invalida
        self.assertRaises(ValueError, self.__test_service.add_book, 1, 2, 3, "")

        # carte existenta
        self.assertRaises(ValueError, self.__test_service.add_book, 1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        print("test_add_book done!")

    def test_remove_book(self):
        # caz general
        self.__test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        deleted_book = self.__test_service.remove_book(1)

        self.assertTrue(deleted_book not in self.__test_repo.get_books())
        self.assertEqual(deleted_book, self.__book)

        # cartea nu exista
        self.assertRaises(ValueError, self.__test_service.remove_book, 1)

        print("test_remove_book done!")

    def test_update_book(self):
        # cartea / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_service.update_book, 20, 1, "lord of the rings", "roman fantasy", "tolkien")

        # carte noua invalida
        self.__test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        self.assertRaises(ValueError, self.__test_service.update_book, 1, 0, "", "", "")

        # caz general
        replaced_book = self.__test_service.update_book(1, 2, "The Hobbit", "Roman fantasy", "Tolkien")
        new_book = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

        self.assertTrue(new_book in self.__test_repo.get_books())
        self.assertTrue(replaced_book not in self.__test_repo.get_books())
        self.assertEqual(replaced_book, self.__book)

        print("test_update done!")

    def test_get_book_by_id_recursive(self):
        # cartea / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_service.get_book_by_id_recursive_version, 1)

        # caz general
        self.__test_service.add_book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        found_book = self.__test_service.get_book_by_id_recursive_version(1)

        self.assertEqual(found_book, self.__book)







