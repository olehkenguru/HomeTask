class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.name}, price: {self.price}'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items = "\n".join(f"{item.name}, {self.products[item]} pcs." for item in self.products)
        return f"User: {self.user}\nItems:\n{items}"

    def get_total(self):
        return sum(item.price * self.products[item] for item in self.products)


# cellphone_motorola = Item('Motorola', 30.0, 'old school cellphone', 'small')
# laptop_apple = Item('Macbook', 500.0, 'nice but expensive technique ', 'big')
#
# # print(cellphone_motorola)
# # print(laptop_apple)
#
# buyer_1 = User('Vasia', 'Pupkin', '+380671122333')
# buyer_2 = User('Dart', 'Weider', '+380800100102')
#
# # print(buyer_1)
# # print(buyer_2)
#
# cart = Purchase(buyer_1)
# cart.add_item(cellphone_motorola, 2)
# cart.add_item(laptop_apple, 4)
#
# print(cart)
#
# Example from task

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
assert cart.get_total() == 40