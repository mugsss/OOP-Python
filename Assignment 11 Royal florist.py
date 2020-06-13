# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 03:50:24 2020

@author: Mugdha
"""

#OOPR-Assgn-11
#Start writing your code here
flowers=['Orchid','Rose','Jasmine']
levels=[15,25,40]
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
    
    def validate_flower(self):
        if(self.__flower_name in flowers):
            return True
        else:
            return False
    def validate_stock(self,required_quantity):
        if(required_quantity<=self.__stock_available):
            return True
        else:
            return False
    def sell_flower(self,required_quantity):
        if(self.validate_flower() == True and self.validate_stock(required_quantity) == True):
            self.__stock_available = self.__stock_available - required_quantity
            
    def check_level(self):
        if self.validate_flower():
            
            x = flowers.index(self.__flower_name)
            if(self.__stock_available< levels[x]):
                return True
            else:
                return False
    
    def set_flower_name(self,flower_nm):
        self.__flower_name = flower_nm
        
    def set_price_per_kg(self,price):
        self.__price_per_kg = price
    def set_stock_available(self,stock):
        self.__stock_available = stock
    
    def get_flower_name(self):
        return self.__flower_name
    
    def get_price(self):
        return self.__price_per_kg
    
    def get_stock(self):
        return self.__stock_available
        
f1 = Flower()
f1.set_flower_name("Orchid")
f1.set_price_per_kg(500)
f1.set_stock_available(5)
req_quantity = 3
print(f1.validate_flower())
print(f1.validate_stock(req_quantity))

print(f1.get_flower_name()," before selling ",f1.get_stock())
f1.sell_flower(req_quantity)
print(f1.get_flower_name()," after selling ",f1.get_stock())

print(f1.check_level())
    
