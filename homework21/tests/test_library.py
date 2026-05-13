import pytest
import logging

from source.library import Book
from source.library import Reader

logger = logging.getLogger(__name__)


@pytest.fixture
def book():
    return Book("Never Lie", "Freida Mcfadden", 364)


@pytest.fixture
def reader():
    return Reader("Palina")


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_reserved(book, reader):
    logger.info(f"Reserving the book {book.book_name}")
    book.reserve_book(reader)
    assert book.book_status == "Booked"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_cannot_be_reserved_statusBooked(book, reader):
    book.book_status = "Booked"
    with pytest.raises(ValueError) as exc_info:
        book.reserve_book(reader)
    assert str(exc_info.value) == "The book cannot be booked"


def test_book_cannot_be_reserved_statusIssued(book, reader):
    book.book_status = "Issued"
    with pytest.raises(ValueError) as exc_info:
        book.reserve_book(reader)
    assert str(exc_info.value) == "The book cannot be booked"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_reservation_can_be_cancelled(book, reader):
    book.reserve_book(reader)
    logger.info(f"Cancelling the book {book.book_name} reservation")
    book.cancel_reserve(reader)
    assert book.book_status == "Free"
    assert book.current_holder is None


def test_reservation_cancellation_person_not_matched(book, reader):
    book.reserve_book(reader)
    another_reader = Reader("Alina")
    with pytest.raises(ValueError) as exc_info:
        book.cancel_reserve(another_reader)
    assert str(exc_info.value) == "Person doesn't match"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_issued_booked_status(book, reader):
    book.reserve_book(reader)
    logger.info(f"Getting the book {book.book_name}")
    book.get_book(reader)
    assert book.book_status == "Issued"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_issued_free_status(book, reader):
    book.get_book(reader)
    assert book.book_status == "Issued"
    assert book.current_holder == reader


def test_book_can_not_be_issued_reservation_by_another_reader(book, reader):
    book.reserve_book(reader)
    another_reader = Reader("Alina")
    with pytest.raises(ValueError) as exc_info:
        book.get_book(another_reader)
    assert str(exc_info.value) == "This book has been reserved by another person"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_return(book, reader):
    book.reserve_book(reader)
    book.get_book(reader)
    logger.info(f"Returning the book {book.book_name}")
    book.return_book(reader)
    assert book.book_status == "Free"
    assert book.current_holder is None


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_reserved_reader(reader, book):
    logger.info(f"Reserving the book {book.book_name} from reader side")
    reader.reserve_book(book)
    assert book.book_status == "Booked"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_cancel_reservation_reader(reader, book):
    reader.reserve_book(book)
    logger.info(f"Cancelling the book {book.book_name} from reader side")
    reader.cancel_reserve(book)
    assert book.book_status == "Free"
    assert book.current_holder is None


@pytest.mark.regression
@pytest.mark.smoke
def test_get_book_reader(reader, book):
    reader.reserve_book(book)
    logger.info(f"Getting the book {book.book_name} from reader side")
    reader.get_book(book)
    assert book.book_status == "Issued"
    assert book.current_holder == reader


@pytest.mark.regression
@pytest.mark.smoke
def test_return_book_reader(reader, book):
    reader.reserve_book(book)
    reader.get_book(book)
    logger.info(f"Returning the book {book.book_name} from reader side")
    reader.return_book(book)
    assert book.book_status == "Free"
    assert book.current_holder is None
