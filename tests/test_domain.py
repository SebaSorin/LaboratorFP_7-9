from domain.entities import Book, Reader
from domain.validators import BookValidator, ReaderValidator


def test_book_validator():
    book = Book(1, "Lord of the Rings", "Roman fantasy", "Tolkien")
    book_validator = BookValidator()

    #valid book
    try:
        book_validator.validate(book)
    except ValueError:
        assert False

    #invalid title
    book.set_title("")
    try:
        book_validator.validate(book)
        assert False
    except ValueError:
        assert True

    #invalid description
    book = Book(1, "Lord of the Rings", "", "Tolkien")
    try:
        book_validator.validate(book)
        assert False
    except ValueError:
        assert True

    # invalid author
    book = Book(1, "Lord of the Rings", "Roman fantasy", "")
    try:
        book_validator.validate(book)
        assert False
    except ValueError:
        assert True

def test_reader_validator():
    reader = Reader(200, "John Reader", 1234567890123)
    reader_validator = ReaderValidator()

    #valid reader
    try:
        reader_validator.validate(reader)
        assert True
    except ValueError:
        assert False

    #invalid name
    reader = Reader(200, "", 1234567890123)
    try:
        reader_validator.validate(reader)
        assert False
    except ValueError:
        assert True

    #invalid cnp
    reader = Reader(200, "John Reader", 1234)
    try:
        reader_validator.validate(reader)
        assert False
    except ValueError:
        assert True



if __name__ == "__main__":
    test_book_validator()
    test_reader_validator()

















