import random
import string

lower=0
upper=0
digit=0
special=0
suggestion = ''
name = ''
password = ''

def getPass(length):
    # choose from all lowercase letter, uppercase and special characters
    char = string.punctuation
    char = char.replace("\"", "")
    char = char.replace("\'", "")
    char = char.replace("(", "")
    char = char.replace(")", "")
    char = char.replace("[", "")
    char = char.replace("]", "")
    char = char.replace("{", "")
    char = char.replace("}", "")
    char = char.replace("<", "")
    char = char.replace(">", "")
    char = char.replace("=", "")
    char = char.replace(":", "")
    char = char.replace(";", "")
    char = char.replace("\\", "")
    char = char.replace("_", "")
    char = char.replace("-", "")
    char = char.replace("`", "")
    char = char.replace("|", "")
    char = char.replace("~", "")
    char = char.replace("+", "")
    char = char.replace(".", "")
    char = char.replace("?", "")
    char = char.replace(",", "")
    char = char.replace("/", "")
    characters = string.ascii_letters + string.digits + char
    suggestion = ''.join(random.choice(characters) for i in range(8))
    return suggestion+"@AB"

name = input("Enter your Name: ")
password = input("Enter the Password: ")

if (len(password)>= 8):
    for i in password:
        # counting lowercase alphabets
        if (i.islower()):
            lower+=1

        # counting uppercase alphabets
        if (i.isupper()):
            upper+=1

        # counting digits
        if (i.isdigit()):
            digit+=1

        # counting the mentioned special characters
        if(i=='@'or i=='$' or i=='#' or i=='!' or i=='%' or i=='^' or i=='&' or i=='*'):
            special+=1

    strength = lambda lower, upper, digit, special: lower>=1 and upper>=1 and digit>=1 and special>=1 and lower + upper + digit + special == len(password) #checking if the strength is good or not

    if (strength(lower ,upper ,digit , special)):
      print("Secure Password! Go Ahead and Register.")

    else:
     print("Not Secure Password")
     print("suggestion is :- ", getPass(8))

else:
  print("Password is to small")


#2

list = [3,9,12,18,24,30,33,39]
for x in list:
    if x % 3 != 0:
        q=1
        break
else:
    q=0
if q == 1:
    print("the list is not divisible by 3")
else:
    print("the list is  divisible by 3")

print("\tTable of 15")
for i in range(1,11):
    print(15, 'x', i, '=',15*i)


square_of_even_num = [num*num for num in list if num % 2 == 0]
print("Square of the even numbers present in the list are: ", square_of_even_num,"\n\n")


even_sum = 0
for sub in list:
    for ele in str(sub):

        # adding in particular summation according to value
        if int(ele) % 2 == 0:
            even_sum += int(ele)
print("Even digit sum : " + str(even_sum),"\n\n")

print("Main List = ", list)



