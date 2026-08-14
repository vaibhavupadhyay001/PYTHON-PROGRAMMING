class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.product_id == other.product_id

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price < other.price

    def __repr__(self):
        return (
            f"Product("
            f"id={self.product_id}, "
            f"name='{self.name}', "
            f"price={self.price}"
            f")"
        )








class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)







p1 = Product(1, "Laptop", 80000)
p2 = Product(2, "Mouse", 1000)
p3 = Product(3, "Keyboard", 3000)

cart = Cart()

cart.add(p1)
cart.add(p2)
cart.add(p3)

print(len(cart))
products = [p1, p2, p3]

products.sort()