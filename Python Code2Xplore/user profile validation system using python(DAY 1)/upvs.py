Full_name=input("Enter Full Name: ")
Email_id=input("Enter Email Id: ")
Mobile_Number=input("Enter Mobile Number: ")
Age=int(input("Enter Age: "))
Valid = True
if ' ' in Full_name and Full_name[0]!=' ' and Full_name[len(Full_name)-1]!=' ':
    Valid = True
else:
    Valid = False
if Valid ==True:
    if '@' in Email_id and '.' in Email_id and Email_id[0]!='@':
        Valid = True
    else:
        Valid = False
if Valid == True:
    if len(Mobile_Number)==10 and Mobile_Number.isdigit() and Mobile_Number[0]!=0:
        Valid = True
    else:
        Valid = False
if Valid == True:
    if Age>=18 and Age<=60:
        Valid = True
    else:
        Valid = False
if Valid == True:
    print("User Profile is VALID")
else:
    print("User Profile is NOT VALID")