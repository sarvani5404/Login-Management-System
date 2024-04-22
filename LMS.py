#User login process project
#from abc import ABC
'''class User:
    def __init__(self,name,rollno,email,pswd):
        self.name=name
        self.rollno=rollno
        self.email=email
        self.pswd=pswd
        d={}
        d[rollno]=[name,email,pswd]'''
class Form:
    def __init__(self):
        self.d={}
       
    def register(self,rollno):
        #print(self.d)
       
        for i in self.d.keys():
            if i==rollno:
                print("User already exist!")
                break
        else:#name,email,pswd
            print("User doesnot exist,Please register!")
            self.name=input("Enter Name:")
            self.email=input("Enter Mail id:")
            self.pswd=input("Enter Password:")
            self.d.update({rollno:[self.name,self.email,self.pswd]})
            print("User successfully registered")
            #print(self.d)
            #break
    def login(self,rollno):
       
        for i in self.d.keys():
            if i==rollno:
                print("User found!!")
                self.pswd=input("Enter Password:")
                if self.pswd in self.d[i]:
                    print("Login successful!!")
                else:
                    print("wrong password!!")
                break
        else:
            print("User not found!!")
           
    def display(self):
        print("Displaying User Profile...")
        for rollno,i in self.d.items():
            print("UserId:",rollno,"\nUsername:",i[0],"\nMail id:",i[1])
    def logout(self):
        exit(1)
f=Form()
while True:
    print("1.Register\n2.Login\n3.Display_Profile\n4.Logout")
    ch=int(input("Enter choice:"))
    if ch==1:
        f.register(int(input("Enter Rollno:")))
    elif ch==2:
        f.login(int(input("Enter Rollno:")))
    elif ch==3:
        f.display()
    elif ch==4:
        f.logout()
    else:
        print("Incorrect Choice!!!")
        break
'''f.register(1)
f.register(2)
f.login(1)
f.login(2)
#f.login(1)'''