#OOPR-Assgn-25
#Start writing your code here
class FruitInfo:
    __fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    __fruit_price_list = [100, 800, 70, 110, 600]
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name not in FruitInfo.__fruit_name_list:
            return -1
        else:
            x = FruitInfo.__fruit_name_list.index(fruit_name)
            y = FruitInfo.__fruit_price_list[x]
            return y
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
        

class Purchase:
    __counter= 101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
    
    def get_purchase_id(self):
        return self.__purchase_id
    
    def get_customer(self):
        return self.__customer
        
    def get_quantity(self):
        return self.__quantity
        
    def calculate_price(self):
        if(FruitInfo.get_fruit_price(self.__fruit_name)==-1):
            return -1
        else:
            self.__purchase_id = 'P' + str(Purchase.__counter)
            Purchase.__counter +=1
            price =  FruitInfo.get_fruit_price(self.__fruit_name)*self.__quantity
            a = max(FruitInfo.get_fruit_price_list())
            ind = FruitInfo.get_fruit_price_list().index(a)
            ind2 = FruitInfo.get_fruit_name_list()[ind]
            #print(ind2)
            
            b= min(FruitInfo.get_fruit_price_list())
            ind3 = FruitInfo.get_fruit_price_list().index(b)
            ind4 = FruitInfo.get_fruit_name_list()[ind3]
            #print(ind4)
            if(self.__quantity>1 and self.__fruit_name == ind2):
                price = price - (2/100)*price
                
                    
            if(self.__quantity>=5 and self.__fruit_name == ind4):
                price = price - (5/100)*price
                    
            
            if(self.get_customer().get_cust_type() == 'wholesale'):
                price = price - (10/100)*price
            
            return price
                
                  


class Customer():
    def __init__(self,customer_name,cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type.lower()
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type

c1= Customer("Mugdha","Retailer")
p1 = Purchase(c1,'Orange',6)
print(p1.calculate_price())
