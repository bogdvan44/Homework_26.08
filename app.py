from gen import gen_customer, gen_house_list
from main import gen_recommendations


def app():
    global res
    try:
        c = gen_customer()
        h = gen_house_list()
        res = gen_recommendations(house_list=h, customer=c)
    except Exception:
        return ValueError("Что-то не так.")
    else:
        return ("No conflicts")
    finally:
        print(res)


print(app())