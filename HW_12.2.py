from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    price: int | float
    description: str
    dimensions: str

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


@dataclass
class User:
    name: str
    surname: str
    numberphone: str

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user: User):
        self.products: dict[Item, int] = {}
        self.user = user

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = cnt

    def get_total(self) -> int | float:
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self) -> str:
        lines = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)


lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, "Екземпляр класу User"
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, "Повинно залишатися 60!"
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40