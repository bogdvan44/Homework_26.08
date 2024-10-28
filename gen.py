from random import randint

def gen_house_list() -> list[dict]:
    house_list = []
    for _ in range(20):
        house = {"price": f"{randint(10_000, 150_000)}$",
                 "square": f"{randint(50, 120)}m2"}
        house_list.append(house)
    return house_list

def gen_customer() -> dict:
    customer = {"account": f"{randint(10_000, 150_000)}$",
                "full name": "Ivan Bogdan"}
    return customer















