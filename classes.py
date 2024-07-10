
# Lets create a food truck
class Food:
     def __init__(self, name, price):
         self.name = name
         self.price = price
     
     def showcaseinfo(self):
         print(f"Food name: {self.name} - {self.price}€")

class Pizza(Food):
     def __init__(self, price, toppings):
          super().__init__("Pizza", price)
          self.toppings = toppings


class Burger(Food):
     def __init__(self, price, ingredients):
         super().__init__("Burger", price)
         self.ingredients = ingredients


Order_list = []    

class Order:
    def __init__(self, ordername, items):
        self.ordername = ordername
        self.items = []
    
    def add_food(self, food):
        self.items.append(food)

    def remove_food(self, food):
        self.items.remove(food)
    
    def cancel_order(self):
        print(f"{self.ordername}'s order has been cancelled")
        self.items = []
        self.ordername = ""
        Order_list.remove(self)
        
    def show_order(self):
        print(self.ordername)
        for item in self.items:
          item.showcaseinfo()

    

class Payment:
    def __init__(self, order, payment_type):
        self.order = order
        self.payment_type = payment_type

    def pay(self):
        total = 0
        for item in self.order.items:
            total += item.price
        print(f"Payment of {self.order.ordername}'s order - Total amount is {total}")

    def payment_registered(self):
        print(f"Payment of {self.order.ordername}'s order has been made with {self.payment_type}")
        self.order.cancel_order()

      
