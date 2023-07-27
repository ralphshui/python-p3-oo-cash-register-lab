#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
    
    def add_item(self, title, price, quantity=1):
        i=0
        while (i < quantity):
            self.items.append(title)
            i+=1
        #for i in range(quantity):
            #self.items.append(title)
            #   i+=1 
        self.item_total = (price*quantity)
        self.total += self.item_total

        return self.items
        
    def apply_discount(self):
        if(self.discount > 0):
            self.total =  int(self.total - (self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.") 
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if (len(self.items) > 1):
            self.items.pop()
            self.total = self.total - self.item_total
        else:
            self.total = 0.0

    

   
        