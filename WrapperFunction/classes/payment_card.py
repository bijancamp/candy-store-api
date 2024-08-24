import datetime


class PaymentCard:
    def __init__(self, card_number: str, expiration_date: datetime.date, name: str, security_code: str) -> None:
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.name = name
        self.security_code = security_code
