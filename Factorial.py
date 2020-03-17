#3! = 3*2*1
'''
fact_number = int(input('Enter the number : '))
factorial = 1
if fact_number < 0:
    print('Fatorial for negative numbers not possible')
elif fact_number==1:
    print('Factorial of 0 is 1')
else:
    for i in range(1,fact_number+1):
        factorial = factorial*i
    #print(i)

print(factorial)
'''

def fact(x):
    if x == 0:
        return 1
    else:
        factorial = x*fact(x-1)
        return factorial

factorial=fact(4)

print(factorial)



    
