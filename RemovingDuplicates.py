first_list = str(input('Enter the values: ')).split()

unique_list = []

for unique in first_list:
    if unique not in unique_list:
        unique_list.append(unique)

unique_list.sort()
print(' '.join(unique_list))
    
