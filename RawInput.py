#Raw input is a built in function to python allows to get input from users

#input from user
#name = input('What is your name? : ')
#print('Hello',name)


import statistics


exList = [5,3,2,9,7,9,4,3,1,8,9]

x = statistics.mean(exList)
print(x)

y = statistics.median(exList)
print('Median: ',y)

z = statistics.mode(exList)
print(z)

a = statistics.stdev(exList)
print('standard Deviation: ',a)

b = statistics.variance(exList)
print('Variance: ',a)
