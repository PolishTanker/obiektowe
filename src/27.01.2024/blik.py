from enum import Enum
from datetime import datetime, timedelta
import uuid


class BlikStatus(Enum):
    CREATED = 1
    USED = 2
    CANCELLED = 3
    EXPIRED = 4


class BlikCode:
    def __init__(self, code, account_id, created_at, valid_until, status):
        self.code = code
        self.account_id = account_id
        self.created_at = created_at
        self.valid_until = valid_until
        self.status = status


class PaymentStatus(Enum):
    UNCONFIRMED = 1
    CONFIRMED = 2
    CANCELLED = 3
    TIMEDOUT = 4


class Payment:
    def __init__(self, payment_id, blik_code, amount, description, status):
        self.payment_id = payment_id
        self.blik_code = blik_code
        self.amount = amount
        self.description = description
        self.status = status


class BlikServer:
    def __init__(self):
        self.accounts = {}
        self.blik_codes = {}
        self.payments = {}
        self.blik_code_validity_duration = timedelta(minutes=5)

    def create_account(self, user_id, password):
        account_id = str(uuid.uuid4())
        self.accounts[user_id] = {'account_id': account_id, 'password': password}
        return account_id

    def login(self, user_id, password):
        if user_id in self.accounts and self.accounts[user_id]['password'] == password:
            return str(uuid.uuid4())  # Return a simple authentication code
        else:
            raise ValueError("Invalid credentials")

    def deposit_funds(self, auth_code, amount):
        # Implement deposit logic here using the auth_code
        pass

    def generate_blik_code(self, auth_code):
        account_id = self.get_account_id_from_auth_code(auth_code)
        code = ''.join([str(uuid.uuid4().int)[:6]])  # Generate a simple 6-character code
        created_at = datetime.now()
        valid_until = created_at + self.blik_code_validity_duration
        status = BlikStatus.CREATED
        blik_code = BlikCode(code, account_id, created_at, valid_until, status)
        self.blik_codes[code] = blik_code
        return code

    def confirm_payment(self, blik_code, auth_code):
        if blik_code not in self.blik_codes:
            raise ValueError("Invalid Blik code")

        account_id = self.get_account_id_from_auth_code(auth_code)
        if self.blik_codes[blik_code].account_id != account_id:
            raise ValueError("Authentication code does not match Blik owner")

        # Update payment status to CONFIRMED
        # You need to implement the logic to associate payments with Blik codes
        payment = self.payments.get(blik_code)
        if payment:
            payment.status = PaymentStatus.CONFIRMED
        else:
            raise ValueError("No payment found for the given Blik code")

    def make_payment(self, recipient_user_id, blik_code, amount, description):
        account_id = self.get_account_id_from_auth_code(blik_code)
        payment_id = str(uuid.uuid4())
        status = PaymentStatus.UNCONFIRMED
        payment = Payment(payment_id, blik_code, amount, description, status)
        self.payments[payment_id] = payment
        return payment_id

    def get_account_id_from_auth_code(self, auth_code):
        # You need to implement logic to retrieve the account_id associated with the auth_code
        pass


if __name__ == '__main__':
    server = BlikServer()

    # Example usage
    user_id = "example_user"
    password = "example_password"

    account_id = server.create_account(user_id, password)
    auth_code = server.login(user_id, password)

    blik_code = server.generate_blik_code(auth_code)
    print(f"Generated Blik code: {blik_code}")

    # Assuming you have a recipient_user_id
    recipient_user_id = "recipient_user"
    amount = 100.0
    description = "Example payment"

    payment_id = server.make_payment(recipient_user_id, blik_code, amount, description)
    print(f"Payment ID: {payment_id}")

    # Confirm the payment using the Blik code
    try:
        server.confirm_payment(blik_code, auth_code)
        print("Payment confirmed")
    except ValueError as e:
        print(f"Error confirming payment: {e}")
