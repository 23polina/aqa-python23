import logging
import pytest

from source.bank import Bank

logger = logging.getLogger(__name__)


@pytest.fixture(name="bank")
def fixture_bank():
    return Bank()


@pytest.mark.regression
@pytest.mark.smoke
def test_client_is_created(bank):
    client_id = "00001"
    logger.info("Creating a client")
    bank.register_client(client_id, "Palina", "Novik")
    assert client_id in bank.clients
    assert bank.clients[client_id]["name"] == "Palina"
    assert bank.clients[client_id]["lastname"] == "Novik"


def test_twice_client_creation(bank):
    client_id = "00001"
    bank.register_client(client_id, "Palina", "Novik")
    logger.info("Creating a client again with the same client_id")
    with pytest.raises(ValueError) as exc_info:
        bank.register_client(client_id, "Palina", "Novik")
    assert str(exc_info.value) == "The client has been already registered"


@pytest.mark.regression
@pytest.mark.smoke
def test_deposit_is_created(bank):
    client_id = "00001"
    bank.register_client(client_id, "Palina", "Novik")
    logger.info("Opening a deposit for the client")
    result = bank.open_deposit(client_id, 10000, 1, 12)
    deposit = bank.clients[client_id]["deposit"]
    assert deposit["amount"] == 10000
    assert deposit["years"] == 1
    assert deposit["percentage"] == 12
    assert result == "Deposit is opened with the amount: 10000"


@pytest.mark.regression
def test_deposit_should_not_be_created(bank):
    client_id = "00001"
    logger.info("Trying to open a deposit for NOT registered client")
    with pytest.raises(ValueError) as exc_info:
        bank.open_deposit(client_id, 10000, 1, 12)
    assert str(exc_info.value) == "The client NOT found"


@pytest.mark.regression
@pytest.mark.smoke
def test_rate_is_calculated(bank):
    client_id = "00001"
    bank.register_client(client_id, "Palina", "Novik")
    bank.open_deposit(client_id, 10000, 1, 12)
    logger.info("Calculating the rate for the client")
    calculated_rate = bank.calculate_rate(client_id)
    assert calculated_rate == 11268.25


@pytest.mark.regression
@pytest.mark.smoke
def test_deposit_can_be_closed(bank):
    client_id = "00001"
    bank.register_client(client_id, "Palina", "Novik")
    bank.open_deposit(client_id, 10000, 1, 12)
    logger.info("Closing a deposit for the client")
    result = bank.close_deposit(client_id)
    assert result == "The deposit has been closed"


def test_deposit_cannot_be_closed_with_incorrect_client_id(bank):
    logger.info("Trying to close a deposit for not registered")
    with pytest.raises(ValueError) as exc_info:
        bank.close_deposit(22324)
    assert str(exc_info.value) == "The client NOT found"


def test_deposit_cannot_be_closed_deposit_not_found(bank):
    client_id = "00001"
    bank.register_client(client_id, "Palina", "Novik")
    logger.info("Trying to close a deposit when there is no opened deposit")
    with pytest.raises(ValueError) as exc_info:
        bank.close_deposit(client_id)
    assert str(exc_info.value) == "The client does not have a deposit"
