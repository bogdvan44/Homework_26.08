class Bank:
    def __init__(self):
        self.account = None  # Инициализируем счет как None (закрыт)

    def open_an_account(self):
        # Открываем счёт с балансом 0.
        if self.account is None:
            self.account = 0
            print("Счет открыт.")

    def close_the_account(self):
        # Закрываем счет.
        if self.account is not None:
            self.account = None
            print("Счет закрыт.")

    def replen_account(self, amount):
        # Пополняем счет, если счет открыт.
        if self.account is not None:
            if amount > 0:
                self.account += amount
                print(f"Счет пополнен на {amount}. Текущий баланс: {self.account}.")
            else:
                print("Счет закрыт. Пополнение невозможно.")

    def with_many(self, amount):
        # Снимаем указанную сумму, если счет открыт и достаточно средств
        if self.account is not None:
            if amount > 0:
                if amount <= self.account:
                    self.account -= amount
                    print(f"Снято {amount}. Текущий баланс: {self.account}.")
                else:
                    print("Недостаточно средств на счете.")
            else:
                print("Счет закрыт. Снятие невозможно.")


bank = Bank()
bank.open_an_account()
bank.replen_account(15000)
bank.with_many(3500)
bank.close_the_account()
bank.replen_account(600)


