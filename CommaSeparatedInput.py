str_input = str(input('Enter input in comma separated values : '))

str_list = str_input.split(",")

#print(str_list)

integer_list = []

for i in str_list:
    integer_list.append(float(i))

integer_tupple = tuple(integer_list)


print(integer_list)
print(integer_tupple)
