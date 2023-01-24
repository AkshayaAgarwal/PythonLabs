import numpy as np
a = np.array([[2,1],
              [0,3]])
b = np.array([[5,4],
              [2,-1]])
print("Matrix A")
print(a)
print("Matrix B")
print(b)
#print(type(a))
#(i). A+B
sum1 = np.add(a,b)
print("A+B")
print(sum1)

#(ii). A-B
sub1 = np.subtract(a,b)
print("A-B")
print(sub1)

#(iii). 3*A
mul = np.multiply(3,a)
print("3A")
print(mul)

#(iv). -2*B
mul1 = np.multiply(-2,b)
print("-2B")
print(mul1)


#2

empty = np.zeros((3,3))
print("Null 3*3")
print(empty)

#3

new = np.zeros((3,3), int)
np.fill_diagonal(new,1)
print("Identity matrix of 3*3")
print(new)

#4
#(i)
Name = ('name1', 'name2', 'name3', 'name4', 'name5')
Score = (10, 20, 30, 40, 50)
Attempts = (1,3,2,1,3)
Qualify = ('yes', 'no', 'yes', 'no', 'yes')

data = np.zeros(5, dtype={'names':('Name', 'Score', 'Attempts', 'Qualify'),
                          'formats':('U10', 'i4', 'i4', 'U10')})
data['Name']=Name
data['Score']=Score
data['Attempts']=Attempts
data['Qualify']=Qualify
print("Structured Array")
print(data)
#(ii)
S = np.array(data['Score'])
S1 = np.array(data['Attempts'])
print("Printing column 2 and column 3")
print(S,S1)

#(iii)

index = [0,1,2]
fancy = np.array(data[index])
print('Extract some data using Fancy Indexing and assign as array')
print(fancy)

# (iv)
print("\n\nStatistical Summary of Score\n\n")
print("1. Sum of all Scores = ",np.sum(S))
print("\n2. Average score = ",np.mean(S))
print("\n3. Standard Deviation = ",round(np.std(S),2))
print("\n4. Variance = ",np.var(S))
print("\n5. Minimum Score = ",np.min(S))
print("\n6. Maximum Score = ",np.max(S))
print("\n7. Median Score = ",np.median(S))
print("\n8. Percentile = ",np.percentile(S,S[1]))
print("\n9. Product of scores = ",np.prod(S))
print("\n10. Range of values = ",np.ptp(S))



