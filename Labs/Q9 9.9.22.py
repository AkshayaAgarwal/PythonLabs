import pandas as pd
import numpy as np

import pandas as pd
data = pd.read_excel(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\Q9 09.09.2022\Q8_MortalityDataset excel.xlsx")
data = pd.read_csv(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\06.09.2022 Q8\Q8_MortalityDataset.csv")
variables=len(data.axes[0])
observation=len(data.axes[1])
print("How many variables and observation does the dataset have?")
print(variables)
print(observation)
print("1b.a.All rows and first three columns")
print(data.iloc[0:200,0:3])
print("First 10 rows and all columns")
print(data.iloc[0:10,0:])
print("10 to 15 rows of first and 4th column")
print(data.iloc[10:15,1:4])
print("Observation of 5th row 2nd column")
print(data.iloc[5:6,2:3])
print("1)b.Number of variables and observation does data set have")
print("Find Structure of the created data frame")
print(data.info(200))
print("\nD. 5th row 2nd column")
print(data.iloc[4:5,2:3])

df=pd.DataFrame(data['AGE'])
print(df.sum())
print(df.count())
print(df.mean())

print(df.median())
print(df.median())
print(df.std())
print(df.min())
print(df.max())
print(df.prod())
print(df.cumsum())
print("unique blood groups")
df1=pd.DataFrame(data['BLOOD'].unique())
print(df1)
print("Unique smoke categories")
df2=pd.DataFrame(data['SMOKE'].unique())
print(df2)

print("\n(h)\nCholesterol level above 300 - ")
print((data.query("CHOL > 300")).shape[0])

print("\n(i)\nMean height value for mortality is alive - ")
print((data.query("MORT == 'alive'"))["HEIGHT"].mean())

df3=data[data['BLOOD']=='o']
df4=df3[df3['HEIGHT']==df3['HEIGHT'].max()]
print("Tallest of blood group 'O' 51 is the column name")
print(df4['AGE'])

print("How many nonsmokers are alive who are below 40 years")


df5=data[data['AGE']<40]
df6=df5[df5['SMOKE']=='nonsmo']
print(df6[df6['MORT']=='alive']['MORT'].count())



import matplotlib.pyplot as plt
da=list(data.groupby('BLOOD')['HEIGHT'].mean())

plt.pie(da)
plt.legend(list(data['BLOOD'].unique()))
plt.show()
plt.scatter(data['HEIGHT'],data['WEIGHT'],alpha=1)

plt.xlabel="height"
plt.ylabel="weight"
plt.show()

data['HEIGHT'].plot.line(xlabel='Height',ylabel='freq',color='r')
plt.show()
data['HEIGHT'].plot.line()
plt.show()

plt.bar(list(data['BLOOD'].unique()),data.groupby('BLOOD')['CHOL'].mean(),color='r')
plt.ylabel='BLOOD GRP'
plt.xlabel='cholesterol'
plt.show()




