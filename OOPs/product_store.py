#Design and create an online store for products(name, price)
# track total products being created
# Create a static method to calculate discount on each product based on a % parameter
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self): #instance method
        print(f"price of {self.name} is Rs.{self.price}")

    classmethod
    def get_count(cls):
        print(f"total prodcuts in store = {cls.count}")

p1 = Product("phone", 10_000)
p2 = Product("laptop", 50_000)
p3 = Product("tablet", 20_000)

Product.get_info()


