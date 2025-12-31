from services.rent_service import ServiceRent
from domain.entities import Book, Reader, RentBook
from repos.rent_repo import RepoRentMemory
from repos.book_repo import RepoBookMemory
from repos.reader_repo import RepoReaderMemory


def test_rent_service_rent_book():
    rent_repo = RepoRentMemory()
    book_repo = RepoBookMemory()
    reader_repo = RepoReaderMemory()
    test_service = ServiceRent(rent_repo, book_repo, reader_repo)
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    book_repo.add(book1)
    book_repo.add(book2)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)
    reader_repo.add(reader1)
    reader_repo.add(reader2)

    rental1 = RentBook(book1, reader1)
    test_service.rent_book(book1.get_id(), reader1.get_id())
    assert rental1 in rent_repo.get_rentals()
    assert rent_repo.get_size() == 1

    #carte non-existenta
    book3 = Book(3, "Atomic Habits", "Carte self-help", "James Clear")
    try:
        test_service.rent_book(book3.get_id(), reader1.get_id())
        assert False
    except ValueError:
        assert True

    # cititor non-existent
    reader3 = Reader(10000, "Richard", 1234577890123)
    try:
        test_service.rent_book(book2.get_id(), reader3.get_id())
        assert False
    except ValueError:
        assert True

    #carte deja inchiriata
    try:
        test_service.rent_book(book1.get_id(), reader2.get_id())
        assert False
    except ValueError:
        assert True

def test_rent_service_return_book():
    test_repo = RepoRentMemory()
    book_repo = RepoBookMemory()
    reader_repo = RepoReaderMemory()
    test_service = ServiceRent(test_repo, book_repo, reader_repo)
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    book_repo.add(book1)
    book_repo.add(book2)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)
    reader_repo.add(reader1)
    reader_repo.add(reader2)

    rental1 = RentBook(book1, reader1)
    test_service.rent_book(book1.get_id(), reader1.get_id())

    del_rental = test_service.return_book(book1.get_id(), reader1.get_id())
    assert test_repo.get_size() == 0
    assert not del_rental in test_repo.get_rentals()
    assert rental1 == del_rental

    #inchiriere non-existenta
    try:
        test_service.return_book(book2.get_id(), reader1.get_id())
        assert False
    except ValueError:
        assert True

    #carte non-existenta
    book3 = Book(3, "Atomic Habits", "Carte self-help", "James Clear")
    try:
        test_service.rent_book(book3.get_id(), reader1.get_id())
        assert False
    except ValueError:
        assert True

    # cititor non-existent
    reader3 = Reader(10000, "Richard", 1234577890123)
    try:
        test_service.rent_book(book2.get_id(), reader3.get_id())
        assert False
    except ValueError:
        assert True

def test_rent_service_get_most_rented_books():
    rent_repo = RepoRentMemory()
    book_repo = RepoBookMemory()
    reader_repo = RepoReaderMemory()
    test_service = ServiceRent(rent_repo, book_repo, reader_repo)

    #mai putin de n (=3) carti
    try:
        test_service.get_most_rented_books_list()
        assert False
    except ValueError:
        assert True

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
    book_repo.add(book1)
    book_repo.add(book2)
    book_repo.add(book3)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)
    reader3 = Reader(4, "Richard", 1111111111111)
    reader_repo.add(reader1)
    reader_repo.add(reader2)
    reader_repo.add(reader3)

    test_service.rent_book(book1.get_id(), reader1.get_id())
    test_service.return_book(book1.get_id(), reader1.get_id())
    test_service.rent_book(book1.get_id(), reader2.get_id())

    test_service.rent_book(book2.get_id(), reader2.get_id())
    """
    book1 = rented 2 times
    book2 = rented once
    book3 = rented 0 times
    """
    dto_list = test_service.get_most_rented_books_list()
    assert rent_repo.get_book_rent_counter() == dto_list[0].get_counter()
    assert dto_list[0].get_book() == book1
    assert dto_list[1].get_book() == book2
    assert dto_list[2].get_book() == book3

def test_rent_service_get_most_rented_readers():
    rent_repo = RepoRentMemory()
    book_repo = RepoBookMemory()
    reader_repo = RepoReaderMemory()
    test_service = ServiceRent(rent_repo, book_repo, reader_repo)

    #mai putin de n (=3) cititori
    try:
        test_service.get_most_rented_readers_list()
        assert False
    except ValueError:
        assert True

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
    book_repo.add(book1)
    book_repo.add(book2)
    book_repo.add(book3)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)
    reader3 = Reader(4, "Richard", 1111111111111)
    reader_repo.add(reader1)
    reader_repo.add(reader2)
    reader_repo.add(reader3)

    test_service.rent_book(book1.get_id(), reader1.get_id())
    test_service.return_book(book1.get_id(), reader1.get_id())
    test_service.rent_book(book1.get_id(), reader2.get_id())

    test_service.rent_book(book2.get_id(), reader2.get_id())
    """
    reader2 = rented 2 times
    reader1 = rented once
    reader3 = rented 0 times
    """
    dto_list = test_service.get_most_rented_readers_list()
    assert rent_repo.get_reader_rent_counter() == dto_list[0].get_counter()
    assert dto_list[0].get_reader() == reader2
    assert dto_list[1].get_reader() == reader1
    assert dto_list[2].get_reader() == reader3

def test_rent_service_get_most_rented_books_by_most_rented_readers():
    rent_repo = RepoRentMemory()
    book_repo = RepoBookMemory()
    reader_repo = RepoReaderMemory()
    test_service = ServiceRent(rent_repo, book_repo, reader_repo)

    # mai putin de n (=3) carti
    try:
        test_service.get_most_rented_books_list()
        assert False
    except ValueError:
        assert True

    # mai putin de n (=3) cititori
    try:
        test_service.get_most_rented_readers_list()
        assert False
    except ValueError:
        assert True

    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
    book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
    book_repo.add(book1)
    book_repo.add(book2)
    book_repo.add(book3)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)
    reader3 = Reader(4, "Richard", 1111111111111)
    reader_repo.add(reader1)
    reader_repo.add(reader2)
    reader_repo.add(reader3)

    test_service.rent_book(book1.get_id(), reader1.get_id())
    test_service.rent_book(book2.get_id(), reader2.get_id())
    test_service.rent_book(book3.get_id(), reader3.get_id())

    test_service.return_book(book1.get_id(), reader1.get_id())
    test_service.return_book(book2.get_id(), reader2.get_id())
    test_service.return_book(book3.get_id(), reader3.get_id())

    test_service.rent_book(book1.get_id(), reader2.get_id())
    test_service.return_book(book1.get_id(), reader2.get_id())

    test_service.rent_book(book1.get_id(), reader3.get_id())
    test_service.return_book(book1.get_id(), reader3.get_id())

    test_service.rent_book(book2.get_id(), reader1.get_id())
    test_service.rent_book(book3.get_id(), reader1.get_id())


    """
    book1 = rented 3
    book2 = rented 2
    book3 = rented 2 
    
    reader1 = rented 3
    reader2 = rented 2 
    reader3 = rented 2
    
    book1 <-> reader1
    book2 <-> reader2
    book3 <-> reader3
    """
    dto_dict = test_service.get_most_rented_books_by_most_rented_readers()
    assert len(dto_dict) == 3
    assert dto_dict[book1.get_id()] == reader1
    assert dto_dict[book2.get_id()] == reader2
    assert dto_dict[book3.get_id()] == reader3


"""if __name__ == "__main__":
    test_rent_service_rent_book()
    test_rent_service_return_book()
    test_rent_service_get_most_rented_books()
    test_rent_service_get_most_rented_readers()
    test_rent_service_get_most_rented_books_by_most_rented_readers()"""


import unittest


class TestCaseRentService(unittest.TestCase):
    def setUp(self):
        self.__rent_repo = RepoRentMemory()
        self.__book_repo = RepoBookMemory()
        self.__reader_repo = RepoReaderMemory()
        self.__test_service = ServiceRent(self.__rent_repo, self.__book_repo, self.__reader_repo)
        self.__book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        self.__book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")
        self.__book_repo.add(self.__book1)
        self.__book_repo.add(self.__book2)

        self.__reader1 = Reader(200, "John Reader", 1234567890123)
        self.__reader2 = Reader(10, "Jane Doe", 9876543210123)
        self.__reader_repo.add(self.__reader1)
        self.__reader_repo.add(self.__reader2)

    def tearDown(self):
        del self.__rent_repo
        del self.__book_repo
        del self.__reader_repo
        del self.__test_service
        del self.__book1
        del self.__book2
        del self.__reader1
        del self.__reader2

    def test_rent_book(self):
        rental1 = RentBook(self.__book1, self.__reader1)
        self.__test_service.rent_book(self.__book1.get_id(), self.__reader1.get_id())

        self.assertTrue(rental1 in self.__rent_repo.get_rentals())
        self.assertEqual(self.__rent_repo.get_size(), 1)

        # carte non-existenta
        book3 = Book(3, "Atomic Habits", "Carte self-help", "James Clear")
        self.assertRaises(ValueError, self.__test_service.rent_book, book3.get_id(), self.__reader1.get_id())


        # cititor non-existent
        reader3 = Reader(10000, "Richard", 1234577890123)
        self.assertRaises(ValueError, self.__test_service.rent_book, self.__book2.get_id(), reader3.get_id())

        # carte deja inchiriata
        self.assertRaises(ValueError, self.__test_service.rent_book, self.__book1.get_id(), self.__reader2.get_id())

    def test_return_book(self):
        rental1 = RentBook(self.__book1, self.__reader1)
        self.__test_service.rent_book(self.__book1.get_id(), self.__reader1.get_id())

        del_rental = self.__test_service.return_book(self.__book1.get_id(), self.__reader1.get_id())
        self.assertEqual(self.__rent_repo.get_size(), 0)
        self.assertTrue(not del_rental in self.__rent_repo.get_rentals())
        self.assertEqual(rental1, del_rental)

        # inchiriere non-existenta
        self.assertRaises(ValueError, self.__test_service.return_book, self.__book2.get_id(), self.__reader1.get_id())

        # carte non-existenta
        book3 = Book(3, "Atomic Habits", "Carte self-help", "James Clear")
        self.assertRaises(ValueError, self.__test_service.rent_book, book3.get_id(), self.__reader1.get_id())

        # cititor non-existent
        reader3 = Reader(10000, "Richard", 1234577890123)
        self.assertRaises(ValueError, self.__test_service.rent_book, self.__book2.get_id(), reader3.get_id())

    def test_get_most_rented_books(self):
        # mai putin de n (=3) carti
        self.assertRaises(ValueError, self.__test_service.get_most_rented_books_list)


        book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
        self.__book_repo.add(book3)

        reader3 = Reader(4, "Richard", 1111111111111)
        self.__reader_repo.add(reader3)

        self.__test_service.rent_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.return_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.rent_book(self.__book1.get_id(), self.__reader2.get_id())

        self.__test_service.rent_book(self.__book2.get_id(), self.__reader2.get_id())
        """
        book1 = rented 2 times
        book2 = rented once
        book3 = rented 0 times
        """
        dto_list = self.__test_service.get_most_rented_books_list()
        self.assertEqual(self.__rent_repo.get_book_rent_counter(), dto_list[0].get_counter())
        self.assertTrue(dto_list[0].get_book() == self.__book1)
        self.assertTrue(dto_list[1].get_book() == self.__book2)
        self.assertTrue(dto_list[2].get_book() == book3)

    def test_get_most_rented_readers(self):
        # mai putin de n (=3) cititori
        self.assertRaises(ValueError, self.__test_service.get_most_rented_readers_list)


        book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
        self.__book_repo.add(book3)

        reader3 = Reader(4, "Richard", 1111111111111)
        self.__reader_repo.add(reader3)

        self.__test_service.rent_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.return_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.rent_book(self.__book1.get_id(), self.__reader2.get_id())

        self.__test_service.rent_book(self.__book2.get_id(), self.__reader2.get_id())
        """
        reader2 = rented 2 times
        reader1 = rented once
        reader3 = rented 0 times
        """
        dto_list = self.__test_service.get_most_rented_readers_list()
        self.assertTrue(self.__rent_repo.get_reader_rent_counter() == dto_list[0].get_counter())
        self.assertTrue(dto_list[0].get_reader() == self.__reader2)
        self.assertTrue(dto_list[1].get_reader() == self.__reader1)
        self.assertTrue(dto_list[2].get_reader() == reader3)

    def test_get_most_rented_books_by_most_rented_readers(self):
        # mai putin de n (=3) carti
        self.assertRaises(ValueError, self.__test_service.get_most_rented_books_list)

        # mai putin de n (=3) cititori
        self.assertRaises(ValueError, self.__test_service.get_most_rented_readers_list)


        book3 = Book(3, "Atomic Habits", "Self-help", "James Clear")
        self.__book_repo.add(book3)

        reader3 = Reader(4, "Richard", 1111111111111)
        self.__reader_repo.add(reader3)

        self.__test_service.rent_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.rent_book(self.__book2.get_id(), self.__reader2.get_id())
        self.__test_service.rent_book(book3.get_id(), reader3.get_id())

        self.__test_service.return_book(self.__book1.get_id(), self.__reader1.get_id())
        self.__test_service.return_book(self.__book2.get_id(), self.__reader2.get_id())
        self.__test_service.return_book(book3.get_id(), reader3.get_id())

        self.__test_service.rent_book(self.__book1.get_id(), self.__reader2.get_id())
        self.__test_service.return_book(self.__book1.get_id(), self.__reader2.get_id())

        self.__test_service.rent_book(self.__book1.get_id(), reader3.get_id())
        self.__test_service.return_book(self.__book1.get_id(), reader3.get_id())

        self.__test_service.rent_book(self.__book2.get_id(), self.__reader1.get_id())
        self.__test_service.rent_book(book3.get_id(), self.__reader1.get_id())

        """
        book1 = rented 3
        book2 = rented 2
        book3 = rented 2 

        reader1 = rented 3
        reader2 = rented 2 
        reader3 = rented 2

        book1 <-> reader1
        book2 <-> reader2
        book3 <-> reader3
        """
        dto_dict = self.__test_service.get_most_rented_books_by_most_rented_readers()
        self.assertTrue(len(dto_dict) == 3)
        self.assertTrue(dto_dict[self.__book1.get_id()] == self.__reader1)
        self.assertTrue(dto_dict[self.__book2.get_id()] == self.__reader2)
        self.assertTrue(dto_dict[book3.get_id()] == reader3)












