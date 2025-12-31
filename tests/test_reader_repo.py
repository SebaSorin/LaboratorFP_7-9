from domain.entities import Reader
from repos.reader_repo import RepoReaderMemory, RepoReaderFile
import unittest

def test_reader_repo_add():
    test_repo = RepoReaderMemory()
    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10,  "Jane Doe",    9876543210123)

    test_repo.add(reader1)
    assert test_repo.get_size() == 1
    assert reader1 in test_repo.get_readers()
    #cititor existent
    try:
        test_repo.add(reader1)
        assert False
    except ValueError:
        assert True

    test_repo.add(reader2)
    assert test_repo.get_size() == 2
    assert reader2 in test_repo.get_readers()

def test_reader_repo_remove():
    test_repo = RepoReaderMemory()
    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    test_repo.add(reader1)
    test_repo.add(reader2)

    #id gresit
    try:
        test_repo.remove(11)
        assert False
    except ValueError:
        assert True

    assert test_repo.get_size() == 2

    removed_reader = test_repo.remove(200)
    assert test_repo.get_size() == 1
    assert removed_reader == reader1

    removed_reader = test_repo.remove(10)
    assert test_repo.get_size() == 0
    assert removed_reader == reader2

    #memorie goala
    try:
        test_repo.remove(4000)
        assert False
    except ValueError:
        assert True

def test_reader_repo_update():
    test_repo = RepoReaderMemory()
    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    #memorie goala
    try:
        test_repo.update(200, reader2)
        assert False
    except ValueError:
        assert True

    test_repo.add(reader1)
    updated_reader = test_repo.update(200, reader2)
    assert test_repo.get_size() == 1
    assert updated_reader == reader1

    #id gresit
    try:
        test_repo.update(100, reader1)
        assert False
    except ValueError:
        assert True

    test_repo.add(reader1)
    #cititor nou existent
    try:
        test_repo.update(10, reader2)
        assert False
    except ValueError:
        assert True

def test_reader_repo_get_reader_by_id():
    test_repo = RepoReaderMemory()
    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    test_repo.add(reader1)
    found_reader = test_repo.get_reader_by_id(reader1.get_id())
    assert found_reader == reader1

    #cititor non-existent
    try:
        test_repo.get_reader_by_id(reader2.get_id())
        assert False
    except ValueError:
        assert True


"""if __name__ == "__main__":
    test_reader_repo_add()
    test_reader_repo_remove()
    test_reader_repo_update()
    test_reader_repo_get_reader_by_id()"""


class TestCaseRepoReaderMemory(unittest.TestCase):
    def setUp(self):
        self.__test_repo = RepoReaderMemory()
        self.__reader = Reader(200, "John Reader", 1234567890123)

    def tearDown(self):
        del self.__test_repo
        del self.__reader

    def test_add(self):
        # caz general
        self.__test_repo.add(self.__reader)
        self.assertEqual(self.__test_repo.get_size(), 1)
        self.assertTrue(self.__reader in self.__test_repo.get_readers())

        # cititor existent in memorie
        self.assertRaises(ValueError, self.__test_repo.add, self.__reader)

        print("test_add done!")

    def test_remove(self):
        # cititorul / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.remove, self.__reader.get_id())

        # caz general
        self.__test_repo.add(self.__reader)
        deleted_reader = self.__test_repo.remove(self.__reader.get_id())

        self.assertEqual(deleted_reader, self.__reader)
        self.assertEqual(self.__test_repo.get_size(), 0)
        self.assertTrue(deleted_reader not in self.__test_repo.get_readers())

        print("test_remove done!")

    def test_update(self):
        old_reader = self.__reader
        new_reader = Reader(10, "Jane Doe", 9876543210123)

        # cititorul / id-ul vechi nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.update, old_reader.get_id(), new_reader)

        # cititorul nou existent in memorie
        self.__test_repo.add(old_reader)
        self.__test_repo.add(new_reader)

        self.assertRaises(ValueError, self.__test_repo.update, old_reader.get_id(), new_reader)

        # caz general
        self.__test_repo.remove(new_reader.get_id())
        removed_reader = self.__test_repo.update(old_reader.get_id(), new_reader)

        self.assertEqual(removed_reader, old_reader)
        self.assertTrue(new_reader in self.__test_repo.get_readers())
        self.assertTrue(old_reader not in self.__test_repo.get_readers())

        print("test_update done!")

    def test_get_by_id(self):
        # cititorul / id-ul lipseste din memorie
        self.assertRaises(ValueError, self.__test_repo.get_reader_by_id, self.__reader.get_id())

        # caz general
        self.__test_repo.add(self.__reader)
        found_reader = self.__test_repo.get_reader_by_id(self.__reader.get_id())

        self.assertEqual(found_reader, self.__reader)

        print("test_get_by_id done")

class TestCaseRepoReaderFile(unittest.TestCase):
    def setUp(self):
        test_file_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/tests/test_reader.txt"
        self.__test_repo = RepoReaderFile(test_file_path)
        self.__reader = Reader(200, "John Reader", 1234567890123)

    def tearDown(self):
        with open(self.__test_repo.get_file_name(), "w") as file:
            pass
        del self.__test_repo

    def test_add(self):
        # caz general
        self.__test_repo.add(self.__reader)
        self.assertEqual(self.__test_repo.get_size(), 1)
        self.assertTrue(self.__reader in self.__test_repo.get_readers())

        # cititor existent in memorie
        self.assertRaises(ValueError, self.__test_repo.add, self.__reader)

        print("test_add_f done!")

    def test_remove(self):
        # cititorul / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.remove, self.__reader.get_id())

        # caz general
        self.__test_repo.add(self.__reader)
        deleted_reader = self.__test_repo.remove(self.__reader.get_id())

        self.assertEqual(deleted_reader, self.__reader)
        self.assertEqual(self.__test_repo.get_size(), 0)
        self.assertTrue(deleted_reader not in self.__test_repo.get_readers())

        print("test_remove_f done!")

    def test_update(self):
        old_reader = self.__reader
        new_reader = Reader(10, "Jane Doe", 9876543210123)

        # cititorul / id-ul vechi nu apare in memorie
        self.assertRaises(ValueError, self.__test_repo.update, old_reader.get_id(), new_reader)

        # cititorul nou existent in memorie
        self.__test_repo.add(old_reader)
        self.__test_repo.add(new_reader)

        self.assertRaises(ValueError, self.__test_repo.update, old_reader.get_id(), new_reader)

        # caz general
        self.__test_repo.remove(new_reader.get_id())
        removed_reader = self.__test_repo.update(old_reader.get_id(), new_reader)

        self.assertEqual(removed_reader, old_reader)
        self.assertTrue(new_reader in self.__test_repo.get_readers())
        self.assertTrue(old_reader not in self.__test_repo.get_readers())

        print("test_update_f done!")

    def test_get_by_id(self):
        # cititorul / id-ul lipseste din memorie
        self.assertRaises(ValueError, self.__test_repo.get_reader_by_id, self.__reader.get_id())

        # caz general
        self.__test_repo.add(self.__reader)
        found_reader = self.__test_repo.get_reader_by_id(self.__reader.get_id())

        self.assertEqual(found_reader, self.__reader)

        print("test_get_by_id_f done")













