def calcAge(year,month,day):
    print("The age is ",2022-year)
    
    
    
while True:         
    try:
        bday = input("Enter your Date of Birth ")
        day, month, year = bday.split("/")
        print(calcAge(int(year), int(month), int(day)))
        break

    except Exception as e:
        if (bday=='?'):
            print("Enter birthday in the given format dd/mm/yy")
        if (bday==' '):
            print("Enter enter your birthday")
        if ((bday=='Q')or(bday=='q')):
            print("Bye!Hope you run This program again")
            break
    except ValueError:
        print("Enter integers in the correct format")





#2 
import re
def MyScottishAccent(s):
    ns = re.sub(r'o', 'u', s)
    print(ns)
i = 1
n = int(input("enter how many sentences you want to check "))
while(i<=n):
    s = input("Enter the sentence : ")
    MyScottishAccent(s)
    i+=1

#3
def LonelyOne(num):
    print("\nEntered number is = ",num)
    count = 0
    a = re.search("11",num)
    if a:
        print(0)
    else:
        for i in range(len(num)):
            if num[i]=="1":
                count+=1
        print(f"1 is lonely {count} times.\n") if count!=0 else print("0")

LonelyOne("101")
LonelyOne("1111")
LonelyOne("444")
