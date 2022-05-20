import json
from os import write

print("WELCOME TO LOGIN/SIGNUP\nEnter 1 for login\nEnter 2 for sign up \n")
ls=int(input("please enter="))
if ls==1:
    l, u, p, d = 0, 0, 0, 0
    name = str(input("Enter Your Name : "))
    email = str(input("Enter Your Email : "))
    i=int(0)
    while i<=0:
        if "@" not in email:
            print("your email is wrong!!")
            break
        else:
            pass
        password = str(input("Enter Your Password(6 character,catipal letter,small letter,special character,number) : "))
        if (len(password) >= 6):
            for i in password:
                if (i.islower()):
                    l+=1			
                if (i.isupper()):
                    u+=1			
                if (i.isdigit()):
                    d+=1			
                if(i=='@'or i=='#'):
                    p+=1		
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
            print(name,"Yor are logged in  Successfully")
            break
        else:
            print("Invalid Password")
            break
        # i+=1
    a=open("details.json" , "a")
    # data=a.write(name)
    # data=a.write(email)
    # data=a.write(password)
    a.close()
    x={}
    x["name"]=name
    x["email"]=email
    x["password"]=password
    k=json.dumps(x,indent=1)
    f1=open("details.json","a")
    f1.writelines(k)
    f1.write("\n")
    f1.write("\n")
    f1.close()
    print() 
    print(x)
    
else:
    l, u, p, d = 0, 0, 0, 0
    name2 = str(input("Enter Your Name : "))
    surname2 = str(input("Enter Your Surname : "))
    email2 = str(input("Enter Your Email : "))
    i=int(0)
    while i<=0:
        if "@" not in email2:
            print("your email is wrong!!")
            break
        else:
            pass
        password2 = str(input("Enter Your Password(6 character,catipal letter,small letter,special character,number) : "))
        if (len(password2) >= 6):
            for i in password2:
                if (i.islower()):
                    l+=1			
                if (i.isupper()):
                    u+=1			
                if (i.isdigit()):
                    d+=1			
                if(i=='@'or i=='#'):
                    p+=1		
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password2)):
            # print("Valid Password")
            confPassword2 = str(input("Confirm Your Password : "))
            if(password2 == confPassword2):
                print("Congrats,",name2,"Yor are Signed up Successfully")
            else:
                print("User Rejected! Invalid Password Combination")
            break
        else:
            print("enter strong Password")
            break
    a=open("details.json" , "a")
    data=a.write(name2)
    data=a.write(email2)
    data=a.write(password2)
    a.close()
    x={}
    x["name"]=name2
    x["surname"]=surname2
    x["email"]=email2
    x["password"]=password2
    x["confpassword"]=confPassword2
    print(x)  









