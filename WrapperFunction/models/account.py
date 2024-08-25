from pydantic import BaseModel


class AccountCheckoutBase(BaseModel):
    status: str

class AccountCheckoutResponse(AccountCheckoutBase):
    pass
