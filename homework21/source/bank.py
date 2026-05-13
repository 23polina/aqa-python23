import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Bank:

    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name, lastname):
        if client_id not in self.clients:
            self.clients[client_id] = {
                "name": name,
                "lastname": lastname
            }
            logger.info(f"{self.clients[client_id]['name']} is registered")
            return self.clients[client_id]
        else:
            raise ValueError("The client has been already registered")

    def open_deposit(self, client_id, amount, years, percentage):
        if client_id not in self.clients:
            raise ValueError("The client NOT found")
        else:
            self.clients[client_id]["deposit"] = {
                "amount": amount,
                "years": years,
                "percentage": percentage
            }
            logger.info("The deposit opened")
            return f"Deposit is opened with the amount: {amount}"

    def calculate_rate(self, client_id):
        client = self.clients[client_id]
        amount = client["deposit"]["amount"]
        percentage = client["deposit"]["percentage"]
        years = client["deposit"]["years"]
        calculated_rate = round(amount * (1 + (percentage / 100) / 12) ** (12 * years), 2)
        logging.info("The rate is calculated")
        return calculated_rate

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            raise ValueError("The client NOT found")
        else:
            client = self.clients[client_id]
        if "deposit" in client:
            del client["deposit"]
            logging.info("The deposit has been closed")
            return "The deposit has been closed"
        else:
            raise ValueError("The client does not have a deposit")
