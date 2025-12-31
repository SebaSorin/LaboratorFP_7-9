from domain.entities import Reader
from repos.reader_repo import RepoReaderMemory
from services.reader_service import ServiceReader


def test_reader_service_add_reader():
    test_repo = RepoReaderMemory()
    test_service = ServiceReader(test_repo)

    reader1 = Reader(200, "John Reader", 1234567890123)

    test_service.add_reader(200, "John Reader", 1234567890123)
    assert test_repo.get_size() == 1
    assert reader1 in test_repo.get_readers()

    #id existent
    try:
        test_service.add_reader(200, "Jane Doe", 9876543210123)
        assert False
    except ValueError:
        assert True

    #cititor invalid
    try:
        test_service.add_reader(4, "", 20)
        assert False
    except ValueError:
        assert True

def test_reader_service_remove_reader():
    test_repo = RepoReaderMemory()
    test_service = ServiceReader(test_repo)

    reader1 = Reader(200, "John Reader", 1234567890123)

    test_service.add_reader(200, "John Reader", 1234567890123)
    test_service.add_reader(10, "Jane Doe", 9876543210123)

    deleted_reader = test_service.remove_reader(200)
    assert test_repo.get_size() == 1
    assert deleted_reader == reader1
    assert not reader1 in test_repo.get_readers()

    #cititor non-existent
    try:
        test_service.remove_reader(1234)
        assert False
    except ValueError:
        assert True

def test_reader_service_update_reader():
    test_repo = RepoReaderMemory()
    test_service = ServiceReader(test_repo)

    reader1 = Reader(200, "John Reader", 1234567890123)
    reader2 = Reader(10, "Jane Doe", 9876543210123)

    test_service.add_reader(200, "John Reader", 1234567890123)
    replaced_reader = test_service.update_reader(200, 10, "Jane Doe", 9876543210123)
    assert test_repo.get_size() == 1
    assert not replaced_reader in test_repo.get_readers()
    assert replaced_reader == reader1
    assert reader2 in test_repo.get_readers()

    #cititor vechi non-existent
    try:
        test_service.update_reader(14, 200, "John Reader", 1234567890123)
        assert False
    except ValueError:
        assert True

    #cititor nou existent
    test_service.add_reader(200, "John Reader", 1234567890123)
    try:
        test_service.update_reader(10, 200, "John Reader", 1234567890123)
        assert False
    except ValueError:
        assert True

    #cititor nou invalid
    try:
        test_service.update_reader(10, 4000000, "", 5)
        assert False
    except ValueError:
        assert True

def test_reader_service_get_reader_by_id():
    test_repo = RepoReaderMemory()
    test_service = ServiceReader(test_repo)

    reader1 = Reader(200, "John Reader", 1234567890123)
    test_service.add_reader(200, "John Reader", 1234567890123)
    found_reader = test_service.get_reader_by_id(200)
    assert found_reader == reader1

    #cititor non-existent
    try:
        test_service.get_reader_by_id(191)
        assert False
    except ValueError:
        assert True

def test_reader_service_generate_reader():
    test_repo = RepoReaderMemory()
    test_service = ServiceReader(test_repo)

    gen_book = test_service.get_random_reader(1)
    assert gen_book == test_service.get_random_reader(1)

    gen_book = test_service.get_random_reader(45)
    assert gen_book == test_service.get_random_reader(45)

    gen_book = test_service.get_random_reader(10000)
    assert gen_book == test_service.get_random_reader(10000)

"""if __name__ == "__main__":
    test_reader_service_add_reader()
    test_reader_service_remove_reader()
    test_reader_service_update_reader()
    test_reader_service_get_reader_by_id()
    test_reader_service_generate_reader()"""

import unittest


class TestCaseReaderService(unittest.TestCase):
    def setUp(self):
        self.__test_repo = RepoReaderMemory()
        self.__test_service = ServiceReader(self.__test_repo)
        self.__reader = Reader(200, "John Reader", 1234567890123)

    def tearDown(self):
        del self.__reader
        del self.__test_repo
        del self.__test_service

    def test_add_reader(self):
        # caz general
        self.__test_service.add_reader(200, "John Reader", 1234567890123)

        self.assertTrue(self.__reader in self.__test_repo.get_readers())

        # cititor invalid
        self.assertRaises(ValueError, self.__test_service.add_reader, 1, "", 3)

        # cititor existent
        self.assertRaises(ValueError, self.__test_service.add_reader, 200, "John Reader", 1234567890123)

        print("test_add_reader done!")

    def test_remove_reader(self):
        # caz general
        self.__test_service.add_reader(200, "John Reader", 1234567890123)
        deleted_reader = self.__test_service.remove_reader(200)

        self.assertTrue(deleted_reader not in self.__test_repo.get_readers())
        self.assertEqual(deleted_reader, self.__reader)

        # cititorul nu exista
        self.assertRaises(ValueError, self.__test_service.remove_reader, 1)

        print("test_remove_reader done!")

    def test_update_reader(self):
        # cititorul / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_service.update_reader, 200, 10, "Jane Doe", 9876543210123)

        # cititor nou invalid
        self.__test_service.add_reader(200, "John Reader", 1234567890123)

        self.assertRaises(ValueError, self.__test_service.update_reader, 200, 0, "", 2)

        # caz general
        replaced_reader = self.__test_service.update_reader(200, 10, "Jane Doe", 9876543210123)
        new_reader = Reader(10, "Jane Doe", 9876543210123)

        self.assertTrue(new_reader in self.__test_repo.get_readers())
        self.assertTrue(replaced_reader not in self.__test_repo.get_readers())
        self.assertEqual(replaced_reader, self.__reader)

        print("test_update_reader done!")

    def test_get_reader_by_id_recursive(self):
        # cititorul / id-ul nu apare in memorie
        self.assertRaises(ValueError, self.__test_service.get_reader_by_id_recursive_version, 1)

        # caz general
        self.__test_service.add_reader(200, "John Reader", 1234567890123)
        found_reader = self.__test_service.get_reader_by_id_recursive_version(200)

        self.assertEqual(found_reader, self.__reader)





