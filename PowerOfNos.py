# Question 2 - 
# Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 



import pandas as pd
n = [int(input('Enter a number :')) for _ in range(5)]    
list=[]
for i in n:
    power= i**2                                             
    list.append(power)
values = pd.Series(list,index=n)       
print(values)
