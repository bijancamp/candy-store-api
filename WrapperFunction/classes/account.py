import uuid

from enum import Enum

import bcrypt


class AccountType(Enum):
    ADMIN = 1
    MEMBER = 2
    GUEST = 3


class Account:
    def __init__(self, name: str, email: str, shipping_address=None, billing_address=None, payment_card=None, account_type='GUEST', past_orders=None) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.payment_card = payment_card
        self.account_type = account_type
        self.past_orders = past_orders

    def _hashPassword(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self._hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    def register(self, password: str) -> None:
        self._hashPassword(password)

        # Continue registration process...

    def checkout(self) -> None:
        if not self.payment_card:
            raise ValueError("No linked payment card")

        # Eventually call _submitPayment...

        return "SHIPPED"

    def _submitPayment(self) -> None:
        pass

    def login(self, password: str) -> None:
        if bcrypt.checkpw(password.encode('utf-8'), self._hashed_password):
            print("Password matches. Logged in.")
        else:
            print("Password does not match. Not logged in.")

    def logout(self) -> None:
        pass

    def delete(self) -> None:
        pass
