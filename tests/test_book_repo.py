from domain.entities import Book
from repos.book_repo import RepoBookMemory, RepoBookFile
import unittest


def test_book_repo_add():
    test_repo = RepoBookMemory()
    book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

    test_repo.add(book)
    assert test_repo.get_size() == 1
    assert book in test_repo.get_books()
    #carte existenta
    try:
        test_repo.add(book)
        assert False
    except ValueError:
        assert True

    book = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_repo.add(book)
    assert test_repo.get_size() == 2
    assert book in test_repo.get_books()

def test_book_repo_remove():
    test_repo = RepoBookMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_repo.add(book1)
    test_repo.add(book2)

    try:
        test_repo.remove(3)
        assert False
    except ValueError:
        assert True

    removed_book = test_repo.remove(1)
    assert test_repo.get_size() == 1
    assert removed_book == book1

    removed_book = test_repo.remove(2)
    assert test_repo.get_size() == 0
    assert removed_book == book2

def test_book_repo_update():
    test_repo = RepoBookMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_repo.add(book1)
    test_repo.add(book2)

    #carte noua existenta
    try:
        test_repo.update(1, book2)
        assert False
    except ValueError:
        assert True

    #id vechi gresit
    new_book = Book(3, "Atomic Habits", "Carte self-help", "James Clear")
    try:
        test_repo.update(3, new_book)
        assert False
    except ValueError:
        assert True

    test_repo.update(2, new_book)
    assert test_repo.get_size() == 2
    assert new_book in test_repo.get_books()
    assert not book2 in test_repo.get_books()

def test_book_repo_get_book_by_id():
    test_repo = RepoBookMemory()
    book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book2 = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

    test_repo.add(book1)
    found_book = test_repo.get_book_by_id(book1.get_id())
    assert found_book == book1

    #carte non-existenta
    try:
        test_repo.get_book_by_id(book2.get_id())
        assert False
    except ValueError:
        assert True

"""if __name__ == "__main__":
    test_book_repo_add()
    test_book_repo_remove()
    test_book_repo_update()
    test_book_repo_get_book_by_id()"""

if __name__ == "__main__":
    unittest.main()


class TestCaseBookRepoMemory(unittest.TestCase):
    def setUp(self):
        self.__test_repo = RepoBookMemory()

    def tearDown(self):
        del self.__test_repo

    def test_add(self):
        # caz general

        book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        self.__test_repo.add(book)

        self.assertEqual(self.__test_repo.get_size(), 1)
        self.assertTrue(book in self.__test_repo.get_books())

        # carte existenta
        self.assertRaises(ValueError, self.__test_repo.add, book)
        print("test_add done!")

    def test_remove(self):
        # carte care nu exista in memorie
        book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        self.assertRaises(ValueError, self.__test_repo.remove, book1.get_id())

        # caz general
        self.__test_repo.add(book1)
        deleted_book = self.__test_repo.remove(book1.get_id())

        self.assertEqual(deleted_book, book1)
        self.assertEqual(self.__test_repo.get_size(), 0)
        self.assertTrue(book1 not in self.__test_repo.get_books())

        print("test_remove done!")

    def test_update(self):
        old_book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        new_book = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

        # cartea veche nu exista in memorie / id-ul cartii vechi nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.update, old_book.get_id(), new_book)

        # id-ul cartii noi apare in memorie
        self.__test_repo.add(old_book)
        self.__test_repo.add(new_book)

        self.assertRaises(ValueError, self.__test_repo.update, old_book.get_id(), new_book)

        # caz general
        self.__test_repo.remove(new_book.get_id())
        deleted_book = self.__test_repo.update(old_book.get_id(), new_book)

        self.assertEqual(deleted_book, old_book)
        self.assertTrue(new_book in self.__test_repo.get_books())
        self.assertTrue(old_book not in self.__test_repo.get_books())
        self.assertEqual(self.__test_repo.get_size(), 1)

        print("test_update done!")

    def test_get_book_by_id(self):
        book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        # cartea/id-ul nu exista in memorie
        self.assertRaises(ValueError, self.__test_repo.get_book_by_id, book.get_id())

        # caz general
        self.__test_repo.add(book)
        found_book = self.__test_repo.get_book_by_id(book.get_id())

        self.assertEqual(found_book, book)
        self.assertTrue(found_book in self.__test_repo.get_books())

        print("test_get_by_id done!")

class TestCaseBookRepoFile(unittest.TestCase):
    def setUp(self):
        test_file_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/tests/test_book.txt"
        self.__test_repo = RepoBookFile(test_file_path)

    def tearDown(self):
        with open(self.__test_repo.get_file_name(), "w") as file:
            pass
        del self.__test_repo

    def test_add(self):
        # caz general

        book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        self.__test_repo.add(book)

        self.assertEqual(self.__test_repo.get_size(), 1)
        self.assertTrue(book in self.__test_repo.get_books())

        # carte existenta
        self.assertRaises(ValueError, self.__test_repo.add, book)
        print("test_add done!")

    def test_remove(self):
        # carte care nu exista in memorie
        book1 = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        self.assertRaises(ValueError, self.__test_repo.remove, book1.get_id())

        # caz general
        self.__test_repo.add(book1)
        deleted_book = self.__test_repo.remove(book1.get_id())

        self.assertEqual(deleted_book, book1)
        self.assertEqual(self.__test_repo.get_size(), 0)
        self.assertTrue(book1 not in self.__test_repo.get_books())
        print("test_remove done!")

    def test_update(self):
        old_book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
        new_book = Book(2, "The Hobbit", "Roman fantasy", "Tolkien")

        # cartea veche nu exista in memorie / id-ul cartii vechi nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.update, old_book.get_id(), new_book)

        # id-ul cartii noi apare in memorie
        self.__test_repo.add(old_book)
        self.__test_repo.add(new_book)

        self.assertRaises(ValueError, self.__test_repo.update, old_book.get_id(), new_book)

        # caz general
        self.__test_repo.remove(new_book.get_id())
        deleted_book = self.__test_repo.update(old_book.get_id(), new_book)

        self.assertEqual(deleted_book, old_book)
        self.assertTrue(new_book in self.__test_repo.get_books())
        self.assertTrue(old_book not in self.__test_repo.get_books())
        self.assertEqual(self.__test_repo.get_size(), 1)

        print("test_update done!")

    def test_get_book_by_id(self):
        book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")

        # cartea/id-ul nu exista in memorie
        self.assertRaises(ValueError, self.__test_repo.get_book_by_id, book.get_id())

        # caz general
        self.__test_repo.add(book)
        found_book = self.__test_repo.get_book_by_id(book.get_id())

        self.assertEqual(found_book, book)
        self.assertTrue(found_book in self.__test_repo.get_books())

        print("test_get_by_id done!")









