products = []


def add_product(name,  expiration_date=None, quantity=1):
    products.append({
        'name': name,
        'expiration_date': expiration_date,
        'quantity': quantity,
    })


def edit_product(name, new_expiration_date = None, new_quantity=None):
    for product in products:
        if product['name'] == name:
            if new_expiration_date:
                product['expiration_date'] = new_expiration_date
            if new_quantity:
                product['quantity'] = new_quantity
            return True
        return False


def delete_product(name):
    global products
    products = [p for p in products if p['name'] != name]


def get_products():
    return products

