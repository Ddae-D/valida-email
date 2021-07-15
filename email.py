import numpy as np
import math as mt
#------------------------------------------------------------------------------------------------
class Welcome():
    def __init__(self):
        self.titleMain= '*** validacion de correo electronico ***'
        
    def welcome(self):
        print("****************************************")
        print(self.titleMain.title())#convertion inline of text special for search
        print("****************************************")
#------------------------------------------------------------------------------------------------
class EmailValidate(): #class 
        
    def __init__(self,arg): #constructor
        self.__mail = arg #arg in self.__email

    def __controlEmail(self): #function private
        print("*** email validating ***")
        try:
            if((" " in self.__mail) or ((self.__mail[0].isdigit() != False))):
                print("Error en la escritura del correo")        
            print("your email is :", self.__mail)
        except Exception as e:
            print("*** exception is : ", e , " ***")

    def controlEmail(self): #function public, tell to system, give me to __controlEmail
        self.__controlEmail()
#------------------------------------------------------------------------------------------------
"""class Test(Welcome):
    print("Ejemplo clase Test")"""
    
#------------------------------------------------------------------------------------------------
w = Welcome().welcome()
arg = input("*** enter your email: ").casefold()   
e = EmailValidate(arg).controlEmail()
