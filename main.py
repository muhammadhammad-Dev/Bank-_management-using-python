
import json
from pathlib import Path
import random
import string



class Bank:
    database=Path('data.json')
    data=[]
    try:
        if (database).exists():
            with open(database,"r") as fs:
                data=json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as e:
        print(f"An error occured as {e}")
    
    @classmethod
    def __update(cls):
        with open(Bank.database,"w")as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generatenumber(cls):
        char=random.choices(string.ascii_letters,k=3)
        dig=random.choices(string.digits,k=5)
        spec=random.choices("!@#$%^&*",k=1)
        result=char+dig+spec
        random.shuffle(result)
        return "".join(result)

    

    def CreateAcoount(self):
        info={
            "Name": input("Enter your name:"),
            "Age":int(input("Enter your age:")),
            "Email": input("Enter your Email:"),
            "Pin":int(input("Enter your 4 digit pin:")),
            "AccountNo.": Bank.__generatenumber(),
            "Balance": 0

        }

        if info["Age"]<18 or len(str(info["Pin"])) != 4:
            print("Sorry you cannot create account")
        else:
            print("Account Created Succesfully...")
            for i in info:
                print(f"{i}, {info[i]}")
            Bank.data.append(info)
            Bank.__update()
    
    def deposite(self):
        Acc_no=input("Enter your account number: ")
        Acc_pin=int(input("Enter your account pin: "))

        userdata=[i for i in Bank.data  if i['AccountNo.']==Acc_no and i["Pin"]==Acc_pin]

        if userdata==False:
            print("Sorry no data founds")
        else:
            amount=int(input("Enter how much money you want to deposite: "))
            if amount>10000 or amount<0:
                print("Sorry not deposite greater than 10000 ammount and less than 0")
            else:
                userdata[0]['Balance']+=amount
                Bank.__update()
                print("Amount deposite succesfully")

    def withdraw(self):
        Acc_no=input("Enter your account number: ")
        Acc_pin=int(input("Enter your account pin: "))

        userdata=[i for i in Bank.data  if i['AccountNo.']==Acc_no and i["Pin"]==Acc_pin]

        if userdata==False:
            print("Sorry no data founds")
        else:
            amount=int(input("Enter how much money you want to withdraw: "))
            if userdata[0]['Balance']< amount: 
                print("Sorry not withdraw your account has less money")
            else:
                userdata[0]['Balance']-=amount
                Bank.__update()
                print("Amount withdraw succesfully")


    def details(self):
        Acc_no=input("Enter your account number: ")
        Acc_pin=int(input("Enter your account pin: "))

        userdata=[i for i in Bank.data  if i['AccountNo.']==Acc_no and i["Pin"]==Acc_pin]

        
        print("YOUR INFORMATION \n\n")

        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
    
    def updatedetails(self):
        Acc_no=input("Enter your account number: ")
        Acc_pin=int(input("Enter your account pin: "))

        userdata=[i for i in Bank.data  if i['AccountNo.']==Acc_no and i["Pin"]==Acc_pin]
        if userdata== False:
            print("No data found")
        else:
            print("You can't change the account no. , balance, age")
            newdata={
            "Name": input("Enter new change name or press enter for skip: "),
            "Email":input("Enter new change email or press enter for skip: "),
            "Pin": input("Enter new change pin or press enter for skip:")
        }
        if newdata["Name"]=="":
            newdata["Name"]=userdata[0]["Name"]
        if newdata["Email"]=="":
            newdata["Email"]=userdata[0]["Email"]
        if newdata["Pin"]=="":
            newdata["Pin"]=userdata[0]["Pin"]

        if type(newdata["Pin"])==str:
            newdata["Pin"]=int(newdata["Pin"])

        newdata["Age"]=userdata[0]["Age"]
        newdata["Balance"]=userdata[0]["Balance"]
        newdata["AccountNo."]=userdata[0]["AccountNo."]

        for i in newdata:
            if newdata[i]==userdata[0][i]:
                continue
                
            else:
                userdata[0][i]=newdata[i]
        
        Bank.__update()
        print("Details Updated Sucesfully")

    def delete(self):
        Acc_no=input("Enter your account number: ")
        Acc_pin=int(input("Enter your account pin: "))

        userdata=[i for i in Bank.data  if i['AccountNo.']==Acc_no and i["Pin"]==Acc_pin]
        if not userdata:
            print("No such data found")
            
        else:

            response=input("Press y for account deletion otherwise press n: ")
            
            if response=="n" or response=="N":
                    print("Ok by passed")
            else:
            
                target_data=userdata[0]
                ind=Bank.data.index(target_data)
                Bank.data.pop(ind)
            
                # #Bank.data.remove(target_data)
                print("Account delete successfully")
                Bank.__update()
      



    
        



    
        

        






    


print("Press 1 for creating an account:")
print("Press 2 for Deposite an account:")
print("Press 3 for Withdraw an account:")
print("Press 4 for deatils  an account:")
print("Press 5 for updating details an account:")
print("Press 6 for deleting an account:")

check=int(input("Enter your response: "))


user=Bank()

if check==1:
    user.CreateAcoount()
if check==2:
    user.deposite()
if check==3:
    user.withdraw()
if check==4:
    user.details()
if check==5:
    user.updatedetails()
if check==6:
    user.delete()
    

