# Импортируем необходимые библиотеки
from typing import List, Dict, Any

users_db = {}
products_db = [{'id': 1, 'name': 'Электрогриль', 'description': 'GR1001 2200Вт', 'price': 140,},
    {'id': 2, 'name': 'Электрогриль', 'description': 'STING 2400Вт', 'price': 157},
    {'id': 3, 'name': 'Электрогриль', 'description': 'MARTA 2500Вт', 'price': 132},]
orders_db = {}

# Функция для хэширования пароля
def hash_password(password):
    key = "$#@4333"
    password_ord = [ord(i) for i in password]
    hash_key = sum([ord(i) for i in key])
    hash_password = ''.join([chr(i + hash_key) for i in password_ord])
    return hash_password
#print(hash_password('1336567ee'))
# Функция для валидации email
def validate_email(email: str):
    valid_domain_zone = ('.ru', '.com', '.by')
    # Проверяем наличие @ в домене
    if '@' not in email:
        raise ValueError ("Email is invalid")
    # Проверяем наличие точки в домене
    if '.' not in email.split('@')[-1]:
        raise ValueError("Email is invalid")

    domain_zone = '.' + email.split('@')[-1].split('.')[-1]
    if domain_zone not in valid_domain_zone:
        raise ValueError ("Email is invalid")
    return email
#email = 'bogvan29@gmail.com'
#print(validate_email(email))
# Функция для регистрации пользователя
def register(credentials: dict):
    name = credentials ['name']
    email = credentials ['email']
    password = credentials ['password']

    if not name:
        return ValueError("Field <name> cannot be empty.")
    if not email:
        return ValueError("Field <email> cannot be empty.")

    try:
        email = validate_email(email)
    except ValueError as e:
        return str(e)

    if not password:
       return ValueError("Field <password> cannot be empty.")

    users_db[email] = {'name': name,'password': hash_password(password),
        'cart': [],'orders': []}

    return {'status_code': 200, 'comment': "Регистрация прошла успешно."}
#print(register(credentials))

# Функция для авторизации пользователя
def login(email: str, password: str):
    user = users_db.get(email)
    if user and user['password'] == hash_password(password):
        return {'status_code': 200, 'comment': "Авторизация успешна.", 'user_info': user}
    return {'status_code': 401, 'comment': "Неверные учетные данные."}

# Функция для получения списка товаров
def get_products() -> List[Dict[str, Any]]:
    return products_db

# Функция для добавления товара в корзину
def add_to_cart(email: str, product_id: int):
    user = users_db.get(email)
    product = next((p for p in products_db if p['id'] == product_id), None)

    if not user:
        return {'status_code': 401, 'comment': "Пользователь не авторизован."}

    if not product:
        return {'status_code': 404, 'comment': "Товар не найден."}

    user['cart'].append(product)
    return {'status_code': 200, 'comment': "Товар добавлен в корзину."}

# Функция для оформления заказа
def checkout(email: str, delivery_address: str):
    user = users_db.get(email)

    if not user:
        return {'status_code': 401, 'comment': "Пользователь не авторизован."}

    if not user['cart']:
        return {'status_code': 400, 'comment': "Корзина пуста."}

        # Создаем заказ
    order_id = len(orders_db) + 1
    orders_db[order_id] = {'email': email,'products': user['cart'],
        'delivery_address': delivery_address}

    # Очищаем корзину после оформления заказа
    user['cart'] = []

    return {'status_code': 200, 'comment': "Заказ оформлен успешно.", 'order_id': order_id}

# Функция для просмотра истории заказов
def view_orders(email: str):
    user = users_db.get(email)

    if not user:
        return {'status_code': 401, 'comment': "Пользователь не авторизован."}

    user_orders = [order for order in orders_db.values() if order['email'] == email]

    return {'status_code': 200, 'orders': user_orders}

# Пример использования функций
credentials = {'name': 'Ivan',
    'email': 'bogvan29@gmail.com',
    'password': '1336567ee'}

print(register(credentials))                                                     # Регистрация
print(login('bogvan29@gmail.com', '1336567ee'))                   # Авторизация
print(get_products())                                                            # Получение списка товаров
print(add_to_cart('bogvan29@gmail.com', 1))                       # Добавление товара в корзину
print(checkout('bogvan29@gmail.com', 'ул. Шапошника, д. 32')) # Оформление заказа
print(view_orders('bogvan29@gmail.com'))                                          # Просмотр истории заказов

