print('Номер 10')
class BankError(Exception):
    pass
class InvalidAmountError(BankError):
    pass
class InsufficientFundsError(BankError):
    pass
class AccountBlockError(BankError):
    pass

def withdraw(balance,amount):
    a=balance-amount
    if amount<=0:
        raise InvalidAmountError('Сумма 0 или меньше')
    if amount>balance:
        raise InsufficientFundsError('Недостаточно средств')
    return a

try:
    b=withdraw(10,110)
    print(b)
except BankError as er:
    print(er)
