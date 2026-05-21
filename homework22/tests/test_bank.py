import logging
from unittest.mock import MagicMock
import pytest
from homework21.source.bank import Bank

logger = logging.getLogger(__name__)


class FakeClientStorage:
    def __init__(self):
        self.clients = {}


@pytest.fixture(name="bank")
def fixture_bank():
    return Bank()


@pytest.fixture(name="bank_with_client")
def fixture_bank_fake():
    bank = Bank()
    bank.clients["00001"] = {
        "name": "Palina",
        "lastname": "Novik"
    }
    return bank


@pytest.fixture(name="client_id")
def fixture_client_id():
    client_id = "00001"
    return client_id


@pytest.mark.regression
@pytest.mark.smoke
def test_client_is_created_mocked(bank, client_id):
    bank.register_client = MagicMock()
    bank.register_client(client_id, "Palina", "Novik")
    bank.register_client.assert_called_once_with(
        client_id, "Palina", "Novik"
    )


def test_twice_client_creation(bank, client_id):
    bank.register_client(client_id, "Palina", "Novik")
    logger.info("Creating a client again with the same client_id")
    with pytest.raises(ValueError) as exc_info:
        bank.register_client(client_id, "Palina", "Novik")
    assert str(exc_info.value) == "The client has been already registered"


@pytest.mark.regression
@pytest.mark.smoke
def test_deposit_is_created_mocked(bank_with_client, client_id):
    logger.info("Opening a deposit for the client")
    bank_with_client.clients[client_id]["deposit"] = {
        "amount": 10000,
        "years": 1,
        "percentage": 12
    }
    bank_with_client.open_deposit = MagicMock(return_value="Deposit is opened")
    opening_result = bank_with_client.open_deposit(client_id, 10000, 1, 12)
    deposit = bank_with_client.clients[client_id]["deposit"]
    assert deposit["amount"] == 10000
    assert deposit["years"] == 1
    assert deposit["percentage"] == 12
    assert opening_result == "Deposit is opened"


@pytest.mark.regression
def test_deposit_should_not_be_created(bank, client_id):
    logger.info("Trying to open a deposit for NOT registered client")
    with pytest.raises(ValueError) as exc_info:
        bank.open_deposit(client_id, 10000, 1, 12)
    assert str(exc_info.value) == "The client NOT found"


@pytest.mark.regression
@pytest.mark.smoke
def test_rate_is_calculated_mocked(bank_with_client, client_id):
    bank_with_client.clients[client_id]["deposit"] = {
        "amount": 10000,
        "years": 1,
        "percentage": 12
    }
    bank_with_client.open_deposit = MagicMock(return_value="Opened")
    opening_result = bank_with_client.open_deposit(client_id, 10000, 1, 12)
    logger.info("Calculating the rate for the client")
    calculated_rate = bank_with_client.calculate_rate(client_id)
    assert opening_result == "Opened"
    assert calculated_rate == 11268.25


@pytest.mark.regression
@pytest.mark.smoke
def test_deposit_can_be_closed_mocked(bank_with_client, client_id):
    bank_with_client.clients[client_id]["deposit"] = {
        "amount": 10000,
        "years": 1,
        "percentage": 12
    }
    bank_with_client.open_deposit = MagicMock(return_value="Opened")
    opening_result = bank_with_client.open_deposit(client_id, 10000, 1, 12)
    bank_with_client.open_deposit.assert_called_once_with(
        client_id, 10000, 1, 12
    )
    logger.info("Closing a deposit for the client")
    closing_result = bank_with_client.close_deposit(client_id)
    assert opening_result == "Opened"
    assert closing_result == "The deposit has been closed"


def test_deposit_cannot_be_closed_with_incorrect_client_id(bank):
    logger.info("Trying to close a deposit for not registered")
    with pytest.raises(ValueError) as exc_info:
        bank.close_deposit(22324)
    assert str(exc_info.value) == "The client NOT found"


def test_deposit_cannot_be_closed_deposit_not_found(bank_with_client, client_id):
    logger.info("Trying to close a deposit when there is no opened deposit")
    with pytest.raises(ValueError) as exc_info:
        bank_with_client.close_deposit(client_id)
    assert str(exc_info.value) == "The client does not have a deposit"
