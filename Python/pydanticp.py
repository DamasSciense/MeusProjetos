from pydantic import BaseModel, field_validator, SecretStr, Field, EmailStr

from rich import traceback

from rich import print

traceback.install()

# class Account:
#     def __init__(self, name: str, balance:float):
#         self.name = name
#         self.balance = balance

class Account(BaseModel, validate_assignment=True):
    name: str = Field(..., min_length=3, max_length=50, frozen=True)
    password: SecretStr
    balance: float

    @field_validator("balance")
    def balance_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("Balance must be positive")
        else:
            return value
if __name__ == "__main__":

    account = Account(name="John", password="password", balance=100)
    
    account.balance = -100
    print(account)
    # print(account.name)
    # print(account.balance)
    