import datetime
import pytest

from WrapperFunction.classes.account import Account
from WrapperFunction.classes.payment_card import PaymentCard


def test_checkout():
    # Test checking out
    card = PaymentCard(
        '0123456789012345',
        datetime.date(2026, 1, 1),
        'Willy Wonka',
        '123'
    )

    account = Account(
        name="Willy Wonka",
        email="wonka@wonkaindustries.com",
        account_type="MEMBER",
        payment_card=card
    )

    status = account.checkout()

    assert status == 'SHIPPED'

def test_checkout_without_payment_card():
    # Test checking out without payment card
    account = Account(
        name="Willy Wonka",
        email="wonka@wonkaindustries.com",
        account_type="MEMBER"
    )

    with pytest.raises(ValueError):
        account.checkout()
