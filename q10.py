# wap to input marks of 5 subject and calculate total,percentage,and grade.

rno =input("enter student roll number : ")
sname = input("enter student name : ")
sub1 = int(input("enter marks of html subject :"))
sub2 = int(input("enter marks of et & it subject :"))
sub3 = int(input("enter marks of os subject :"))
sub4 = int(input("enter marks of ps subject :"))
sub5 = int(input("enter marks of rdbms subject :"))

print("\n")
total=sub1+sub2+sub3+sub4+sub5
avg=total/5

print("student roll number is : ",rno)
print("student name is : ",sname)
print("marks of html subject : ",sub1)
print("marks of et & it subject : ",sub2)
print("marks of os subject : ",sub3)
print("marks of ps subject : ",sub4)
print("marks of rdbms subject : ",sub5)
print("\n")
print("total marks : ",total)
print("percentage marks : ",avg)


if(avg>=80):
    print("grade: A+")
elif(avg>=70):
    print("grade: A")
elif(avg>=60):
    print("grade: B")
elif(avg>=50):
    print("grade: C")
elif(avg>=35):
    print("grade: D")
else:
    print("grade : fail")