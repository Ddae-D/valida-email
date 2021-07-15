class EmailValidate(): #class
    def __init__(self,arg): #constructor
        self.__mail = arg #arg in self.__email

    def __controlEmail(self): #function private
        print(self.__mail)

    def testEmail(self): #function public, tell to system, give me to __imprime
        self.__controlEmail()
#
#
arg = input("enter you email: ") #recept email
emaile = EmailValidate(arg) #sent email to constructor
emaile.testEmail() #start function hehe
