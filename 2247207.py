#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[94]:


data = pd.read_csv(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\CAC2\flipkart_smartphones_2022_03_26_2333_IST.csv")
data.head(3)


# In[95]:


data.columns


# In[96]:


row_count=len(data)
print(row_count)
print(data.info()) 


# In[97]:


data['ram'].unique()


# In[98]:


data['ram']


# In[99]:


data.describe() # statical function


# In[100]:


data.isnull().sum()


# In[101]:


data.dropna(inplace=True)
data.isnull().any().any()


# In[102]:


data.nunique()


# In[103]:


data['brand'].unique()


# In[104]:


poco_phone = data[data['brand'] == 'POCO']
poco_phone.head()


# In[105]:


poco_phone[['selling_price','original_price']]


# In[106]:


poco_phone.title.value_counts()


# In[107]:


poco_phone.index = range(len(poco_phone.index))
poco_phone.head()


# In[108]:


poco_phone.tail()


# In[109]:


import warnings
warnings.filterwarnings('ignore')
new = poco_phone.ram.str.split(' ',n=2,expand=True)
poco_phone['ram_val'] = new[0]
poco_phone.head(3)


# In[110]:


plt.figure(figsize=(15,5))
sns.barplot(x=poco_phone['title'],y=poco_phone['avg_rating'], ci=None)
plt.title('Average  Rating of Xiaomi POCO SmartPhones ')
plt.xlabel('MOBILES')
plt.ylabel('AVERAGE RATING')
plt.ylim(ymin=1,ymax=4.7)
plt.xticks(rotation=90)
plt.show()
poco_phone['avg_rating'].max()


# In[111]:


oppo_phone = data[data['brand'] == 'OPPO']
oppo_phone.head()


# In[112]:


bd=data.brand.unique()
#bd.drop['Coolpad', 'Maplin', 'YU','Panasonic', 'Jmax']
ag=[]
ag1=[]
for i in bd:
    if(data[data.brand==i]['brand'].count())>8:
        ag.append(data[data.brand==i]['brand'].count())
        ag1.append(i)
        
print(ag)
print(ag1)
e=(0.0,0.2,0.0,0.0,0.0,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)


# In[113]:


import seaborn
plt.figure(figsize=(20,20))
palette_color = seaborn.color_palette('dark')

plt.pie(ag, labels=ag1,
        explode=e, autopct='%.0f%%',textprops={'fontsize': 16},shadow=True, startangle=140)
plt.axis('equal')

plt.show()


# In[114]:


data=data[data.brand!='Coolpad']
data=data[data.brand!='OPPO']
data=data[data.brand!='Alcatel']
data=data[data.brand!='YU']
data=data[data.brand!='TCL']
data=data[data.brand!='ASUS']
data=data[data.brand!='Panasonic']
data=data[data.brand!='Maplin']
data=data[data.brand!='Jmax']
data=data[data.brand!='KARBONN']
data=data[data.brand!='MarQ By Flipkart']
data=data[data.brand!='ITEL']
data=data[data.brand!='Infinix']
data=data[data.brand!='MOTOROLA']
data=data[data.brand!='Tecno']
data=data[data.brand!='XOLO']




print(data.brand.unique())


# In[115]:



plt.figure(figsize=(15,10))
sns.set(style="darkgrid")

sns.boxplot(data=data, x='brand',y='selling_price')
sns.boxplot(x = "brand",
            y = "selling_price",
            data = data)
sns.stripplot(x = "brand",
              y = "selling_price",
                color = 'black',
              data = data)
plt.ylabel('SELLING PRICE')
plt.xlabel('BRAND')
plt.ylim(5000,60000)
plt.show()


# In[116]:


data=data[data.brand!='realme']
plt.figure(figsize=(20, 10))
sns.set(style="whitegrid")


ax = plt.axes(projection="3d")
ax.scatter3D(data['selling_price'], data['avg_rating'], data['reviews_count'], 
              alpha = 0.4)
ax.set_xlabel("Selling Price")
ax.set_ylabel("Average Ratings")
ax.set_zlabel("Total Ratings")
ax.set_title("Mobiles selling price with their average ratings and total reviews")
plt.show()


# In[117]:


plt.figure(figsize=(25,15))
data=data[data.brand!='Itel']
data=data[data.brand!='LAVA']
data=data[data.brand!='GIONEE']
data=data[data.brand!='Micromax']
sns.set(style="whitegrid")


sns.histplot(data, x="selling_price", hue="brand", element="poly")
plt.show()

