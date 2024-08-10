import csv

class Item:
    discount_rate = 0.2

    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise ValueError("Price cannot be directly updated. Use apply_discount method.")

    def calculate_total_price(self):
        return self._price * self.quantity

    def apply_discount(self):
        self._price = self._price * (1 - Item.discount_rate)

    @classmethod
    def all_items(cls, file_path):
        items = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price, quantity = row[0], float(row[1]), int(row[2])
                item = cls(name, price, quantity)
                item.apply_discount()
                items.append(item)
        return items

    def __str__(self):
        return f"Item(name={self.name}, price={self._price:.2f}, quantity={self.quantity}, total={self.calculate_total_price():.2f})"
