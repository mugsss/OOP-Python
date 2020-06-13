#An apparel shop wants to manage the items which it sells

#OOPR-Assgn-24
#Start writing your code here
class Apparel:
    counter = 100
    def __init__(self,price,item_type):
        Apparel.counter+=1
        self.__item_id=item_type[0].upper()+str(Apparel.counter)
        self.__price = price
        self.__item_type = item_type
       
    def calculate_price(self):
        self.__price= self.__price + 5/100*self.__price
        
        
    def get_item_id(self):
        return self.__item_id
    def  get_price(self):
        return self.__price
    
    def get_item_type(self):
        return self.__item_type
    
    def set_price(self,price):
        self.__price = price
        

class Cotton(Apparel):
    def __init__(self,price,discount):
        Apparel.__init__(self,price,'cotton')
        self.__discount = discount
    def calculate_price(self):
        super().calculate_price()
        price = Apparel.get_price(self)
        price = price - (self.__discount/100)*price
        price = price + (5/100)*price
        Apparel.set_price(self, price)
    def get_discount(self):
        return self.__discount

class Silk(Apparel):
    def __init__(self,price):
        Apparel.__init__(self,price,'silk')
        self.__points = 0
    
    def calculate_price(self):
        super().calculate_price()
        price = Apparel.get_price(self)
        if(price>10000):
            self.__points += 10
        else:
            self.__points += 3
        price = price + (10/100)*price
        Apparel.set_price(self,price)
    def get_points(self):
        return self.__points
        

c1 = Cotton(2000,4)
c1.calculate_price()
