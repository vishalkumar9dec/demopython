Numbers = []

for i in range(2000,3000):
    if (i%7==0) and (i%5!=0):
        Numbers.append(str(i))


#print(Numbers)
print (','.join(Numbers))
