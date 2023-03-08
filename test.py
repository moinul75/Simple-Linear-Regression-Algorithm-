import pandas as pd 
import json 
import matplotlib.pyplot as plt
import math

df = pd.read_csv('./data.csv')
headers = df.columns.values
x =df[headers[0]]
y = df[headers[1]]

x = x.truncate(4900,4999)
y = y.truncate(4900,4999)


#now get the data of m,c 
with open('./train.txt','r') as file:
    data = file.read()
    convert_data = json.loads(data)
    
m = convert_data['m']
c = convert_data['c']
Ymean = convert_data['Y_mean']

predicted_value = []
#now predict all the value 
for val in x:
    y_predict = m*val +c 
    predicted_value.append(y_predict)
    
    
#now check the accurecy by finding the r-squared_value 
Y_pred = []
r_upper = 0 
r_lower = 0
for idx in range(len(y)):
    y_pred = m*x[idx+4900] + c 
    Y_pred.append(y_pred)
    r_upper+=math.pow(y[idx+4900]-y_pred,2)
    r_lower+=math.pow(y[idx+4900]-Ymean,2)
    
r_square_value = 1 -(r_upper/r_lower)
print(r_square_value)
    
    
    
    


#check this using prediction from the input and output section 
inp = int(input("Enter the years of Experience: "))
prediction = m*inp + c
print(f'Your Predicted Salary will be: {prediction} Tk')

    
plt.scatter(x,y,color='g')
plt.title('Salary Prediciton')
plt.ylabel('Salary')
plt.xlabel('Years Of experience')
plt.plot(x,predicted_value,color="r")
plt.show()


    
    





