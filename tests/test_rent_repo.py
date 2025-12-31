from domain.entities import Book, Reader, RentBook
from repos.rent_repo import RepoRentMemory, RepoRentFile

def test_rent_repo_find():
    test_repo = RepoRentMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

    reader1 = Reader(200, "John Reader", 1234567890123)

    rental1 = RentBook(book1, reader1)
    assert test_repo.find(rental1) == False

    test_repo.add(rental1)
    assert test_repo.find(rental1) == True

def test_rent_repo_add():
    test_repo = RepoRentMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    rental1 = RentBook(book1, reader1)
    test_repo.add(rental1)
    assert test_repo.get_size() == 1
    assert rental1 in test_repo.get_rentals()

    assert book1.get_id() in test_repo.get_book_rent_counter()
    assert test_repo.get_book_rent_counter()[book1.get_id()] == 1

    assert reader1.get_id() in test_repo.get_reader_rent_counter()
    assert test_repo.get_reader_rent_counter()[reader1.get_id()] == 1

    #carte existenta
    rental2 = RentBook(book1, reader2)
    try:
        test_repo.add(rental2)
        assert False
    except ValueError:
        assert True

def test_rent_repo_remove():
    test_repo = RepoRentMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    rental1 = RentBook(book1, reader1)
    rental2 = RentBook(book2, reader2)
    test_repo.add(rental1)
    test_repo.add(rental2)

    del_rental = test_repo.remove(rental1)
    assert test_repo.get_size() == 1
    assert not rental1 in test_repo.get_rentals()
    assert del_rental == rental1

    #inchirierea non-existenta
    try:
        test_repo.remove(rental1)
        assert False
    except ValueError:
        assert True



"""if __name__ == "__main__":
    test_rent_repo_add()
    test_rent_repo_find()
    test_rent_repo_remove()"""

import unittest

class TestCaseRepoRentMemory(unittest.TestCase):
    def setUp(self):
        self.__test_repo = RepoRentMemory()
        self.__book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        self.__book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
        self.__reader1 =  Reader(200, "John Reader", 1234567890123)
        self.__reader2 = Reader(10, "Jane Doe", 9876543210123)

    def tearDown(self):
        del self.__test_repo
        del self.__book1
        del self.__book2
        del self.__reader1
        del self.__reader2

    def test_add(self):
        # caz general
        rental1 = RentBook(self.__book1, self.__reader1)
        self.__test_repo.add(rental1)

        self.assertTrue(rental1 in self.__test_repo.get_rentals())
        self.assertTrue(rental1 in self.__test_repo.get_history())
        self.assertEqual(self.__test_repo.get_book_rent_counter()[self.__book1.get_id()], 1)
        self.assertEqual(self.__test_repo.get_reader_rent_counter()[self.__reader1.get_id()], 1)

        # carte inchiriata deja
        rental2 = RentBook(self.__book1, self.__reader2)
        self.assertRaises(ValueError, self.__test_repo.add, rental2)

        print("test_add done!")

    def test_find(self):
        rental = RentBook(self.__book1, self.__reader1)
        self.assertFalse(self.__test_repo.find(rental))

        self.__test_repo.add(rental)
        self.assertTrue(self.__test_repo.find(rental))

        print("test_find done!")

    def test_remove(self):
        rental = RentBook(self.__book1, self.__reader1)

        # inchirierea nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.remove, rental)

        # caz general
        self.__test_repo.add(rental)
        deleted_rental = self.__test_repo.remove(rental)

        self.assertTrue(deleted_rental not in self.__test_repo.get_rentals())
        self.assertEqual(deleted_rental, rental)
        self.assertEqual(self.__test_repo.get_size(), 0)

        print("test_remove done!")

class TestCaseRepoRentFile(unittest.TestCase):
    def setUp(self):
        test_file_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/tests/test_rent.txt"
        self.__test_repo = RepoRentFile(test_file_path)
        self.__book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        self.__book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
        self.__reader1 =  Reader(200, "John Reader", 1234567890123)
        self.__reader2 = Reader(10, "Jane Doe", 9876543210123)

    def tearDown(self):
        with open(self.__test_repo.get_file_name(), "w") as file:
            pass

        del self.__test_repo
        del self.__book1
        del self.__book2
        del self.__reader1
        del self.__reader2

    def test_add(self):
        # caz general
        rental1 = RentBook(self.__book1, self.__reader1)
        self.__test_repo.add(rental1)

        self.assertTrue(rental1 in self.__test_repo.get_rentals())
        self.assertTrue(rental1 in self.__test_repo.get_history())
        self.assertEqual(self.__test_repo.get_book_rent_counter()[self.__book1.get_id()], 1)
        self.assertEqual(self.__test_repo.get_reader_rent_counter()[self.__reader1.get_id()], 1)

        # carte inchiriata deja
        rental2 = RentBook(self.__book1, self.__reader2)
        self.assertRaises(ValueError, self.__test_repo.add, rental2)

        print("test_add done!")

    def test_find(self):
        rental = RentBook(self.__book1, self.__reader1)
        self.assertFalse(self.__test_repo.find(rental))

        self.__test_repo.add(rental)
        self.assertTrue(self.__test_repo.find(rental))

        print("test_find done!")

    def test_remove(self):
        rental = RentBook(self.__book1, self.__reader1)

        # inchirierea nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.remove, rental)

        # caz general
        self.__test_repo.add(rental)
        deleted_rental = self.__test_repo.remove(rental)

        self.assertTrue(deleted_rental not in self.__test_repo.get_rentals())
        self.assertEqual(deleted_rental, rental)
        self.assertEqual(self.__test_repo.get_size(), 0)

        print("test_remove done!")












