# 1. write a python program to find the frequency of every word in the given
# paragraph.
def counting(lines):
    numbers = dict()
    word = lines.split()

    for char in word:
        if char in numbers:
            numbers[char] += 1
        else:
            numbers[char] = 1
    return numbers
print(counting('This is a python lab test'))
print(counting('Hi hi hi hello hello'))


# 2. Write a program to compute the number of characters, words and lines in the
# given paragraph
count = 0
given_details = ("""program for counting the details of this program.
                 Adding one more line to check.""")
test = len(given_details.split())
for lines in given_details:
    if (lines == '.'):
        count += 1
print("the number of lines are ")
print(count)
print("number of words :")
print(str(test))
print("number of character are : ")
print(len(given_details))

# 3. Write a python program to find whether the given string is in alphabetical order
# or not (return true if the input string is in alphabetical order else return false)

def seqeunce(string):
    return ''.join(sorted(string))

string = input("enter any string ")

print(seqeunce(string))
if seqeunce(string) == string:
    print("true")
else:
    print("false")

""" 6. Given the list of CGPA of students CGPA=[9,7,6,5,10,3,9,6,6,4] Write:
a) An expression that evaluates to the number of 6 CGPA
b) A statement that changes the last CGPA to 3
c) An expression that evaluates to the maximum CGPA
d) A statement that sorts the list CGPA
e) An expression that evaluates to the average CGPA
"""
CGPA = [9,7,6,5,10,3,9,6,6,4]
print("total number of times 6 is present is ")
print(CGPA.count(6))
CGPA.remove(4)
CGPA.append(3)
print("After changing the last CGPA to 3 ")
print(CGPA)
print("maxium cgpa is ")
print(max(CGPA))
print("values after sorting ")
print(sorted(CGPA))
s = sum(CGPA)
l = len(CGPA)
avg = s/l
print("The average of the list is ")
print(avg)

"""4. Write a python program to encrypt a given string using the following method:
5. Encrypt Method: Add a number ‘n’(given by the user ) to each alphabet in the
given string to create the corresponding letter.
Example: Input: bat
Encrypt Method:value of n = 3
Output:edu."""

def en(c,n):
    x = " "
    for i in c:
        a = ord(i)
        a += numbers
        x += chr(a)
    return x
words = input("enter the words to check ")
numbers = int(input("enter the number "))

print(en(words,numbers))




