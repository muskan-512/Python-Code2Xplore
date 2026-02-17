Student_id = input("Enter Student ID : ")
Email_id = input("Enter Email ID : ")
Password = input("Enter Password : ")
Referral_code = input("Enter Referral Code : ")
Valid = True
if Student_id.startswith("CSE") and Student_id[3]=='-' and Student_id[4:].isdigit():
    Valid = True
else:
    Valid=False
if Valid == True:
    if '@' in Email_id and '.' in Email_id and Email_id[0]!='@' and Email_id[len(Email_id)-1]!='@' and Email_id.endswith(".edu"):
        Valid = True
    else:
        Valid = False
if Valid == True:
    if len(Password)>=8 and Password[0] == Password[0].upper() and ("0" in Password or "1" in Password or "2" in Password or "3" in Password or
     "4" in Password or "5" in Password or "6" in Password or "7" in Password or "8" in Password or "9" in Password):
        Valid = True
    else:
        Valid = False
if Valid == True:
    if Referral_code.startswith("REF") and Referral_code[3:5].isdigit() and Referral_code[len(Referral_code)-1]== '@':
        Valid = True
    else:
        Valid = False
if Valid == True:
    print("Approved")
else:
    print("Rejected")