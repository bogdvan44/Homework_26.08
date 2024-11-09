class Bank:
    # Создаём класс Баннк с атрибутом начальный баланс 0
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    # применяем декоратор property для получения и установки значения баланса
    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def replein(self, amount):
        self._balance += amount
        # Пополняем баланс
        print(f"Счет пополнен на {amount}")

    def tace(self, amount):
        self._balance -= amount
        # Снимае со счета
        print(f"Со счета снято {amount}")


bank = Bank(500)
print(f"Начальный баланс: {bank.balance}")
bank.replein(1000)
print(f"Баланс после пополнения: {bank.balance}")
bank.tace(500)
print(f"Баланс после снятия: {bank._balance}")

