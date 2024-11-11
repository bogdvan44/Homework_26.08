class Phone:
    def __init__(self, model, colour, cost):
        self._model = model
        self._colour = colour
        self._cost = cost

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, new_colour):
        self._colour = new_colour

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost

    def calculate_discount(self, percent):
        discount = (percent / 100) * self._cost
        return self._cost - discount


phone = Phone("Huawei P40 lite", "black", 650)
print(f"Модель: {phone.model}, Цвет: {phone.colour}, Стоимость: {phone.cost} руб.")

# Устанавливаем новые значения
phone.colour = "white"
phone.cost = 635
print(f"Обновленный цвет: {phone.colour}, Обновленная стоимость: {phone.cost} руб.")

# Вычисляем скидку
discount_percent = phone.calculate_discount(20)
print(f"Стоимость после 20% скидки: {discount_percent} руб.")

