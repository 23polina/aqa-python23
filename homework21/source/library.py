import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Book:

    def __init__(self, book_name, author, pages_amount):
        self.current_holder = None
        self.book_status = "Free"
        self.book_name = book_name
        self.author = author
        self.pages_amount = pages_amount

    def reserve_book(self, person):
        if self.book_status == "Free":
            self.book_status = "Booked"
            self.current_holder = person
            logger.info(f"The {self.book_name} is reserved")
        else:
            raise ValueError("The book cannot be booked")

    def cancel_reserve(self, person):
        if self.book_status == "Booked" and self.current_holder == person:
            self.book_status = "Free"
            self.current_holder = None
            logger.info(f"The reservations has been canceled")
        elif self.book_status == "Booked" and self.current_holder != person:
            raise ValueError("Person doesn't match")

    def get_book(self, person):
        if self.book_status == "Booked" and self.current_holder == person:
            self.book_status = "Issued"
            self.current_holder = person
            logger.info(f"The {self.book_name} has been issued")
        elif self.book_status == "Free":
            self.book_status = "Issued"
            self.current_holder = person
            logger.info(f"The {self.book_name} has been issued")
        elif self.book_status == "Booked" and self.current_holder != person:
            raise ValueError("This book has been reserved by another person")

    def return_book(self, person):
        if self.book_status == "Issued" and self.current_holder == person:
            self.book_status = "Free"
            self.current_holder = None
            logger.info(f"The {self.book_name} has been returned")


class Reader:

    def __init__(self, reader_name):
        self.reader_name = reader_name

    def reserve_book(self, book):
        book.reserve_book(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)



book = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien", pages_amount=322)

palina = Reader("Palina")
petya = Reader("Petya")

palina.reserve_book(book)

