#OOPR-Assgn-20
#Start writing your code here
#OOPR-Assgn-20
#Start writing your code here
class Applicant:
    __application_dict = {'A': 0, 'B': 0, 'C': 5}
    __applicant_id_count = 1000
    def __init__(self,applicant_name):
        self.__applicant_name = applicant_name
        self.__applicant_id = None
        self.__job_band = None
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
    
    def get_applicant_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name
    def get_job_band(self):
        return self.__job_band
    
    def generate_applicant_id(self):
        Applicant.__applicant_id_count= Applicant.__applicant_id_count + 1
        self.__applicant_id = Applicant.__applicant_id_count
        return Applicant.__applicant_id_count
        
    def apply_for_job(self,job_band):
        for key,value in Applicant.get_application_dict().items():
            if(key == job_band):
                if(value < 5):
                    self.get_application_dict()[key] = value+1
                    x = self.generate_applicant_id()
                    self.__job_band = job_band
                
                else:
                    return -1
A1 =Applicant("Jack")
A1.apply_for_job("C")
#print(A1.get_applicant_id())
#print(Applicant.get_application_dict())
print(A1.get_job_band())
