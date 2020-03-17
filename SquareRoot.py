#Program to calculate the square root

import math

d_input = str(input('Enter the values of D in CSV format: '))

d_list_str = d_input.split(",")

d_list_int = []

d_list_sqrt = []

C = 50
H = 30

#print(d_list_str)
for i in d_list_str:
    d_list_int.append(int(i))


for i in d_list_int:
    d_list_sqrt.append(int(math.sqrt((2*C*i)/H)))



#print(d_list_float)
print(d_list_sqrt)

    




