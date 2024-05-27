#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount
        self.last_transaction = 0.0
    
    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([item_name] * quantity)
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."
    
    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0

register = CashRegister(20)
register.add_item("apple", 1.00, 3)
register.add_item("banana", 0.50, 5)
print(register.total) 
print(register.apply_discount())  
register.add_item("grapes", 2.00, 2)
print(register.total)  
register.void_last_transaction()
print(register.total) 

