from items import Item

class Laptop(Item):
    discount_rate = 0.3

    def __init__(self, name, price, quantity, gpu, port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu
        self.port_count = port_count

    def apply_discount(self):
        self._price = self._price * (1 - Laptop.discount_rate)

    def __str__(self):
        return (f"Laptop(name={self.name}, price={self._price:.2f}, quantity={self.quantity}, "
                f"gpu={self.gpu}, port_count={self.port_count}, total={self.calculate_total_price():.2f})")
