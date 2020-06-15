#OOPR-Exer-13
#Start writing your code here
#ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers.A consumer can register for one Base Package.


basePack_name=['Silver','Gold','Platinum']
monthly_rent = [350.00,440.00,560.00]
from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass = ABCMeta):
    __counter = 101
    def __init__(self,consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter=DirectToHomeService.__counter+1
    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    @abstractmethod
    
    def calculate_monthly_rent(self):
        pass
    

class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period
    def get_base_pack_name(self):
        return self.__base_pack_name
    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if(self.get_base_pack_name() not in basePack_name):
            self.__base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")
    def calculate_monthly_rent(self):
        if(self.get_subscription_period()>=1 and self.get_subscription_period()<=24):
            self.validate_base_pack_name()
            x = self.get_base_pack_name()
            index1 = basePack_name.index(x)
            mrent =  monthly_rent[index1]
            
            if(self.get_subscription_period()> 12):
                mrent = ((mrent * self.get_subscription_period()) - mrent)/self.get_subscription_period()
                return mrent
            else: 
                return mrent
        else:
            return -1

b1 = BasePackage("Sita", "Silver", 1) 
#print(b1.get_consumer_name())
b1.calculate_monthly_rent()

