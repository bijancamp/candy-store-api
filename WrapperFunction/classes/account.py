import uuid

import bcrypt

from account_type import AccountType
from address import Address
from cart import Cart
from order import Order
from payment_card import PaymentCard


class Account:
    def __init__(self, name: str, email: str, shipping_address: Address, billing_address: Address, payment_card: PaymentCard, account_type: AccountType, past_orders: list[Order]) -> None:
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

    def checkout(self, cart: Cart) -> None:
        if not self.payment_card:
            raise ValueError("No linked payment card")

        # Eventually call _submitPayment...
        pass

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
