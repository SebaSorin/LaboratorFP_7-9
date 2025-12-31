from repos.book_repo import RepoBookMemory
from repos.book_repo import RepoBookFile
from repos.reader_repo import RepoReaderMemory
from repos.reader_repo import RepoReaderFile
from repos.rent_repo import RepoRentMemory
from repos.rent_repo import RepoRentFile
from services.book_service import ServiceBook
from services.reader_service import ServiceReader
from services.rent_service import ServiceRent
from ui.console import Console

book_default_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/book_default.txt"
reader_default_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/reader_default.txt"
rent_default_path = "C:/Users/40726/PyCharm 2025.2.3/LabFP7_9/rent_default.txt"

while True:
    Console.print_memory_type()
    memory_option = input(">>>").upper()

    if memory_option == "F":
        # memorie pe fisiere
        book_repo = RepoBookFile(book_default_path)
        reader_repo = RepoReaderFile(reader_default_path)
        rent_repo = RepoRentFile(rent_default_path)
        break
    elif memory_option == "T":
        # memorie temporara
        book_repo = RepoBookMemory()
        reader_repo = RepoReaderMemory()
        rent_repo = RepoRentMemory()
        break
    else:
        print("Comanda invalida!")


book_service = ServiceBook(book_repo)
reader_service = ServiceReader(reader_repo)
rent_service = ServiceRent(rent_repo, book_repo, reader_repo)

cons = Console(book_service, reader_service, rent_service)

cons.run()