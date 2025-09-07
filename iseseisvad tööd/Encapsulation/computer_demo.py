class Computer:

    def __init__(self):
        self.name = "Inspiron"
        self.__sellingprice = 700

    def sell(self):
        print(f"{self.name} Selling Price: {self.__sellingprice}")

    def set_selling_price(self, price):
        self.__sellingprice = price

class GamingComputer(Computer):
    def __init__(self):
        super().__init__()
        self.name = "AlienWare"


c = Computer()
c.sell()

# change the price
c.__sellingprice = 1000
c.sell()

# setting selling price using setter function
c.set_selling_price(1000)
c.sell()

gc = GamingComputer()
gc.sell()
gc.__name = "ROG"
gc.sell()