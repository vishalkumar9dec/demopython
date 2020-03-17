input_num = input('Enter the values of X and Y : ')

int_input_values = [ int(x) for x in input_num.split(",")]

#print(input_values)
X = 0
Y = 0
'''
int_input_values = []
for i in input_values:
    int_input_values.append(int(i))
'''

X = int_input_values[0]
Y = int_input_values[1]

list_main = []
list_dynamic = []
for i in range(0,X):
    list_dynamic = []
    for j in range(0,Y):
        list_dynamic.append(i*j)
    list_main.append(list_dynamic)


print(list_main)
print(list_main[2][2])

