class Product:
    def __init__(self, name, price, quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_piece(self):
        self.quantity += 1
        print(f"Now you have {self.quantity} pieces of {self.name}")

    def total_price(self):
        return self.price*self.quantity

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        if product in self.cart:
            idx = self.cart.index(product)
            self.cart[idx].add_piece()
            print(f"Another piece of {self.cart[idx].name} has been added to the cart, now you have {self.cart[idx].quantity} of {self.cart[idx].name}")
        else:
            self.cart.append(product)
            print(f"The product {self.cart[-1].name} has been added to the cart")

    def rmv_product(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"All the pieces of {product.name} have been removed")
        else:
            print("the product is not in the cart")

    def total_cost(self):
        tot_price = 0
        for x in self.cart:
            tot_price += x.total_price()
        return tot_price
    
shoes = Product("Shoes", 80)
hat = Product("Hat", 20)
pullover = Product("pullover", 85)
jeans = Product("Jeans", 120)
pullover.add_piece()
hat.add_piece()
cart = ShoppingCart()

cart.add_product(shoes)
cart.add_product(shoes)
cart.add_product(shoes)
cart.add_product(hat)
cart.rmv_product(hat)
cart.add_product(pullover)
cart.rmv_product(jeans)

print("The total price of your cart is: ", cart.total_cost())

