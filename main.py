
def gen_recommendations(house_list: list[dict], customer: dict)-> list[dict]:
    amount = int(customer["account"][:-1])
    f_houses = []
    for house in house_list:
        house_price = int(house["price"][:-1])
        if house_price <= amount:
            f_houses.append(house)
    f_houses.sort(key=lambda i: int(i["square"][:-2]), reverse=True)
    return f_houses

























