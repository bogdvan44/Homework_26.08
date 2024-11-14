class Restaurant:
    def __init__(self):
        self.menu = []  # Создаём меню как пустой список
        self.order = []  # Создаем заказ как пустой список

    def add_a_dish(self, dish):
        # Добавление блюд в меню.
        self.menu.append(dish)
        print(f"Блюдо '{dish}' добавлено в меню.")

    def remuve_dish(self, dish):
        # Удаление блюд в меню.
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"Блюдо '{dish}' удалено из меню.")

    def to_order(self, dishes):
        # Добавление заказов в список.
        for dish in dishes:
            if dish in self.menu:
                self.order.append(dish)
                print(f"Блюдо '{dish}' добавлено в заказ.")

    def show_the_order(self):
        # Выводим список заказаннных блюд.
        if self.order:
            print("Ваш заказ:")
            for dish in self.order:
                print(f"- {dish}")


restaurant = Restaurant()
restaurant.add_a_dish("Omlet")
restaurant.add_a_dish("Salad")
restaurant.add_a_dish("Cofee")
restaurant.remuve_dish("Salad")
restaurant.to_order(["Omlet", "Cofee"])
restaurant.show_the_order()

