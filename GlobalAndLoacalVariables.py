x=6 #Global Variable

def example3():
    global x
    x+=1
    print(x)

def example():
    z=5 #Local Variable
    print(z)

#cannot do this as z is local variable
#print(z) 

#example()


def example2():
    z=7
    print(z)
    print(x)

    y = x+1
    print(y)
    return y

x = example2()
#print(x)
#example2()

example3()
print(x)

