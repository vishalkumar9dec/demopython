'''raw_input = input('Enter the CSV : ')

str_list = [x for x in raw_input.split(",")]

str_list.sort()

#print(str_list)

print (','.join(str_list))'''

lines = []

print('Enter the input in multi lines : ')

while True:
    test = input()
    if test:
        lines.append(test)
    else:
        break
print('\n'.join(lines).upper())


