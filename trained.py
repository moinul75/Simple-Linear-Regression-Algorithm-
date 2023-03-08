import pandas as pd 
import json 
import math

df = pd.read_csv('data.csv')



#calculate Mean 
def calculate_mean(data):
    sum = 0
    for val in data:
       sum+=val
    mean = sum/len(data)
    return mean


headers = df.columns
x = df[headers[0]]
y = df[headers[1]]

#get 100 data for test 
x = x.truncate(0,4899)
y = y.truncate(0,4899)

Xmean = calculate_mean(x)
Ymean = calculate_mean(y)

#now calcuate x-Xmean,y-Ymean
upper_summetion = 0 
lower_summetion = 0
for idx in range(len(y)):
    upper_summetion+=(x[idx] - Xmean) *(y[idx]-Ymean)
    lower_summetion+=math.pow(x[idx]-Xmean,2)
    
# print(upper_summetion)
# print(lower_summetion)
#now calculate the m 
m = upper_summetion/lower_summetion

#now calcutae the c 
c = Ymean - (m*Xmean)
# print(c)

#get m and c in a dictionary 
trained_data = {}
trained_data['m'] = m
trained_data['c'] = c
trained_data['Y_mean'] = Ymean

with open('train.txt','w') as file:
    file.write(json.dumps(trained_data))
    
    
    
    


