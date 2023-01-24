# working on Dataset
import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\Class\president_heights.csv")
print(data)
data1 = pd.read_csv(r"C:\Users\Akshaya Agarwal\Desktop\christ\python\Class\president_heights1.csv")
#print(data1)
#print(data.head())
#print(data.tail())
heights = np.array(data['height(cm)'])
#print(heights)
a = np.sum(((heights >180)) & ((heights < 189))) #  sum the number of people of this height
print(a)

b = np.sum(~((heights >=180)) & ((heights <=189)))
print(b)
print(np.b.ndim(heights))
short = (heights < 175) # return boolean answers
medium =(heights > 175) & (heights <185)
tall= (heights >=185)

print(short) # printing  in boolean i.e True or False
print(heights[short])# made an array of true values

print("Median height of short residents: ", np.median(heights[short]))
print("maximum height of short residents: ", np.max(heights[short]))
print("Minimum height of short residents: ", np.min(heights[short]))
print("Mean height of short residents: ", np.mean(heights[short]))


print("Median height of medium residents: ", np.median(heights[medium]))
print("maximum height of medium residents: ", np.max(heights[medium]))
print("Minimum height of medium residents: ", np.min(heights[medium]))
print("Mean height of medium residents: ", np.mean(heights[medium]))

print("Median height of tall residents: ", np.median(heights[tall]))
print("maximum height of tall residents: ", np.max(heights[tall]))
print("Minimum height of tall residents: ", np.min(heights[tall]))
print("Mean height of tall residents: ", np.mean(heights[tall]))
