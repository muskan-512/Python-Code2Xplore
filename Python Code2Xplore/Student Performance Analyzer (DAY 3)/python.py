name = input("Enter your name:")
len_Name = len(name)
n= int(input("Enter the number of student in the list:"))
Marks=[0]*n
for i in range(n):
    Marks[i]=int(input("Enter students marks: "))
print("Input Marks:", Marks)
valid_count=0
failed_count=0
for j in Marks:
    if j<0 or j>100:
        print(j,"-> Invalid")
    else:
        valid_count+=1
        if j==78 and len_Name%2==0:
            print(j,"-> Excellent")
        elif j>=90 and j<=100:
            print(j,"-> Excellent")
        elif j>=75 and j<=89:
            print(j,"-> Very Good")
        elif j>=60 and j<=74:
            print(j,"-> Good")
        elif j>=40 and j<=59:
            print(j,"-> Average")
        else:
            print(j,"-> Fail")
            failed_count+=1
print("Final Summary:")
print("Total Valid Student: ", valid_count)
print("Total Failed Student: ",failed_count)