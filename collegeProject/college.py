# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:11:29 2020

@author: Mugdha
"""

# LBJ1 case study1

class College:
    def __init__(self,collegeId , collegeName, courseType , city , fees ,pinCode):
        self.__collegeId = collegeId
        self.__collegeName =  collegeName
        self.__courseType = courseType
        self.__city = city
        self.__fees = fees
        self.__pinCode = pinCode
        
    def get_collegeId(self):
        return self.__collegeId
    
    def get_college_name(self):
        return self.__collegeName
    
    def get_courseType(self):
        return self.__courseType
    
    def get_city(self):
        return self.__city
    
    def get_fees(self):
        return self.__fees
    
    def get_pincode(self):
        return self.__pinCode
    
    
    
    def registerNewCollege(self):
        x1 = self.get_collegeId()
        x2 = self.get_college_name()
        x3 = self.get_courseType()
        x4 = self.get_city()
        x5 = self.get_fees()
        x6 = self.get_pincode()
        list1 = [x1,x2,x3,x4,x5,x6]
        #print(list1)
        index = 0
        dataFile = open(r"C:\Users\Mugdha\Desktop\collegeInfo\collegeData.txt", "a")
        for data in list1:
            index = index+1
            dataFile.write(data)
            if index != (7 - 1):
                dataFile.write(',')
            else:
                dataFile.write('\n')
        
        
        
        dataFile.close()
        
        
    @staticmethod
    def displayEngineeringColleges_in_Mumbai():
        listFind = []
        fh = open(r'C:\Users\Mugdha\Desktop\collegeInfo\collegeData.txt','r')
        for line in fh:
            x = line.split(",")
            listFind.append(x)
        #print(listFind)
        fh.close()
        
        listCollege = []
        for collegeRecord in listFind:
            #print(collegeRecord)
            collegeRecord[2].upper()
            collegeRecord[3].upper()
            if(collegeRecord[2]== 'Engineering' and collegeRecord[3]== 'Mumbai'):
                listCollege.append(collegeRecord[1])
        return listCollege        
        
    @staticmethod    
    def removeCollege(idInput):
        listFind = []
        fh = open(r'C:\Users\Mugdha\Desktop\collegeInfo\collegeData.txt', 'r')
        for line in fh:
            x = line.split(",")
            listFind.append(x)
        
        #print(listFind)
        
        flag = 0
        for record in listFind:
            if (record[0]==idInput):
                flag =1
                a =listFind.index(record)
                #print(a)
                z = listFind.pop(a)
                #print(z)
        if(flag ==0):
            return False
        
        #print(listFind)
        listFind = []
        fh = open(r'C:\Users\Mugdha\Desktop\collegeInfo\collegeData.txt', 'r')
        for line in fh:
            x = line.split(",")
            listFind.append(x)
    
    
        f = open(r'C:\Users\Mugdha\Desktop\collegeInfo\collegeData.txt', "w")
        for a in listFind:
            index = 0
            if a != z:
                a[5] = a[5][0:6]
                #print(a)
                for data in a:
                    index = index+1
                    f.write(data)
                    if index != (7 - 1):
                        f.write(',')
                    else:
                        f.write('\n')
                    #print(index)
                    
        f.close()
        return True
                    
#c1 = College()

class Switcher(object):
    def indirect(self,i):
        method_name='number_'+str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()
    def number_1(self):
        print("Enter the college details")
        input1 = input("Enter the college Id:")
        input2 = input("Enter College Name:")
        input3 = input("Enter Course Type:")
        input4 = input("Enter the City:")
        input5 = input("Enter the Fees:")
        input6 = input("Enter the Pin Code:")
        c1 = College(input1,input2,input3,input4,input5,input6)
        
        c1.registerNewCollege()
        
        return "Registered"
    
    def number_2(self):
        college = College.displayEngineeringColleges_in_Mumbai()
        
        if(len(college) == 0):
            return "No record Found yet for Enginerring colleges in Mumbai "
        else:
            for i in range(0,len(college)):
                print(college[i])
            print("{} record found".format(i+1))
        
    def number_3(self):
        idInput = input("Enter the college Id:")
        #print(idInput)
        p = College.removeCollege(idInput)
        if(p==False):
            print("Record with ID: {} not found".format(idInput))
        else:
            print("Record with ID: {} DELETED".format(idInput))
            
          
            
s=Switcher()
functionality = input("**Enter** \n 1 - register: \n 2 - Display college who has Eng: \n 3 - remove college: \n")
#print(functionality)
s.indirect(functionality)

        
    
        
