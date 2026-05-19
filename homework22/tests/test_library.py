import logging
import random
import pytest
from homework21.source.library import Book
from homework21.source.library import Reader

logger = logging.getLogger(__name__)


@pytest.fixture(name="book")
def fixture_book():
    return Book("Never Lie", "Freida Mcfadden", 364)


class ReaderStub:
    reader_name = "Palina"


@pytest.fixture(name="reader_stub")
def fixture_reader_stub():
    return ReaderStub()


@pytest.fixture(name="reader")
def fixture_reader():
    return Reader("Palina")


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_book_can_be_reserved(book, reader_stub):
    assert random.randint(2, 5) > 3
    logger.info("Reserving the book")
    book.reserve_book(reader_stub)
    assert book.book_status == "Booked"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_cannot_be_reserved_status_booked(book, reader_stub):
    book.book_status = "Booked"
    with pytest.raises(ValueError) as exc_info:
        book.reserve_book(reader_stub)
    assert str(exc_info.value) == "The book cannot be booked"


def test_book_cannot_be_reserved_status_issued(book, reader_stub):
    book.book_status = "Issued"
    with pytest.raises(ValueError) as exc_info:
        book.reserve_book(reader_stub)
    assert str(exc_info.value) == "The book cannot be booked"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_reservation_can_be_cancelled(book, reader_stub):
    book.reserve_book(reader_stub)
    logger.info("Cancelling the book reservation")
    book.cancel_reserve(reader_stub)
    assert book.book_status == "Free"
    assert book.current_holder is None


def test_reservation_cancellation_person_not_matched(book, reader_stub):
    book.reserve_book(reader_stub)
    another_reader = Reader("Alina")
    with pytest.raises(ValueError) as exc_info:
        book.cancel_reserve(another_reader)
    assert str(exc_info.value) == "Person doesn't match"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_issued_booked_status(book, reader_stub):
    book.reserve_book(reader_stub)
    logger.info("Getting the book")
    book.get_book(reader_stub)
    assert book.book_status == "Issued"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_issued_free_status(book, reader_stub):
    book.get_book(reader_stub)
    assert book.book_status == "Issued"
    assert book.current_holder == reader_stub


def test_book_can_not_be_issued_reservation_by_another_reader(book, reader_stub):
    book.reserve_book(reader_stub)
    another_reader = Reader("Alina")
    with pytest.raises(ValueError) as exc_info:
        book.get_book(another_reader)
    assert str(exc_info.value) == "Selected book has been reserved by another person"


@pytest.mark.regression
@pytest.mark.smoke
def test_book_return(book, reader_stub):
    book.reserve_book(reader_stub)
    book.get_book(reader_stub)
    logger.info("Returning the book")
    book.return_book(reader_stub)
    assert book.book_status == "Free"
    assert book.current_holder is None


@pytest.mark.regression
@pytest.mark.smoke
def test_book_can_be_reserved_reader(reader, book):
    logger.info("Reserving the book from reader side")
    reader.reserve_book(book)
    assert book.book_status == "Booked"
    assert book.current_holder.reader_name == "Palina"


@pytest.mark.regression
@pytest.mark.smoke
def test_cancel_reservation_reader(reader, book):
    reader.reserve_book(book)
    logger.info("Cancelling the book from reader side")
    reader.cancel_reserve(book)
    assert book.book_status == "Free"
    assert book.current_holder is None


@pytest.mark.regression
@pytest.mark.smoke
def test_get_book_reader(reader, book):
    reader.reserve_book(book)
    logger.info("Getting the book from reader side")
    reader.get_book(book)
    assert book.book_status == "Issued"
    assert book.current_holder == reader


@pytest.mark.regression
@pytest.mark.smoke
def test_return_book_reader(reader, book):
    reader.reserve_book(book)
    reader.get_book(book)
    logger.info("Returning the book from reader side")
    reader.return_book(book)
    assert book.book_status == "Free"
    assert book.current_holder is None
