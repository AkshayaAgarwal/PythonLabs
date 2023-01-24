import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\06.09.2022 Q8\Q8_MortalityDataset.csv")
age=data['AGE']
height=data['HEIGHT']
weight=data['WEIGHT']
chol=data['CHOL']
smoke=data['SMOKE']
blood=data['BLOOD']
mort=data['MORT']

data1= np.zeros(200,dtype={'names':('age','height', 'weight', 'chol', 'smoke', 'blood', 'mort'),
                          'formats':('i4', 'i4', 'i4', 'i4', 'U10', 'U10', 'U10')})
data1['age']=age
data1['height']=height
data1['weight']=chol
data1['smoke']=smoke
data1['blood']=blood
data1['mort']=mort
print("1)a.----Structured Array----")
print(data1)
print("-------------------------------------")
print("1)b.Number of variables and observation does data set have")
variables=len(data.axes[0])
observation=len(data.axes[1])
print("The number of variables:",variables)
print("The number of observations:",observation)
print("---------------------------------------")

#(c)
# A.
print("\nA. All rows and first three columns\n",data1[['age','height','weight']])

#B. 
print("\nB. First 10 rows and all columns\n",data1[0:10])
#C.
print("\nC. 10 to 15 rows of first and 4th column\n",data1[9:15][['age','chol']])
#D.
print("\nD. 5th row 2nd column\n",data1[4][1])

#(d)
print("\nStructure of the array - ",data1.dtype)

#(e)
arr = np.array([(data1[::]['height']),(data1[::]['weight'])])
print(arr)

#(f)
S = np.array(data1['age'])
S1 = np.array(data1['height'])

print("\n\nStatistical Summary of Score\n\n")
print("1. Sum of all age = ",np.sum(S))
print("\n2. Average age = ",np.mean(S))
print("\n3. Standard Deviation = ",round(np.std(S),2))
print("\n4. Variance = ",np.var(S))
print("\n5. Minimum age = ",np.min(S))
print("\n6. Maximum age = ",np.max(S))
print("\n7. Median age = ",np.median(S))
print("\n8. Percentile = ",np.percentile(S,S[1]))
print("\n9. Product of Age = ",np.prod(S))
print("\n10. Range of age = ",np.ptp(S))


#G
print((len(data['BLOOD'].value_counts())))
print("Number of blood different blood groups are:",len(data['BLOOD'].unique()))

#H
print("Unique smoke categories",data['SMOKE'].unique())

#I
print("cholestrol above 300: ", len(data[data['CHOL']>300]))    

#J
#(j)
mort = np.array(data['MORT'])
bool_array = (mort=='alive')
heights = np.array(data['HEIGHT'])
heights[bool_array]
print("\nMean height value for mortality is alive : ",np.mean(heights))

#K
blood_group = np.array(data['BLOOD'])
bool_2 = (blood_group == 'o')
height = np.array(data['HEIGHT'])
tallest = np.max(height[bool_2])
bool_3 = (height == tallest)
age = np.array(data['AGE'])
print("Age = ",age[bool_3][0])

#L
smoker = np.array(data['SMOKE'])
bool_4 = (age<40) & (smoker == 'nonsmo')
print("No. of non smokers less than 40  years alive = ",len(mort[bool_4]))
