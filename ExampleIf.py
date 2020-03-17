x = 2
y = 7
z = 10

if x > y:
    print(x,'is greater than y')
if x < y:
    print(x,'is less than y')

if x==y:
    print(x,'is equals to',y)


'''
cannot do this
if x < '2':
    print(x,'is less than 2')
'''

if z > y > x:
    print(z,'is greater than',y,'which is greater than',x)

#####################################

x = 3
y = 6

if x < y:
    print(x,'is less than',y)
else:
    print(x,'is not less than',y)
