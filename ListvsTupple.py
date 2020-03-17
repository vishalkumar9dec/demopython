#Tupple is immutable(cannot be changed once defined), example a=(1,2,3,4)
#Tupple mainly used for variable assignment and sequence unpacking, takes less space, cause it is immuateble, faster
#List is mutable and can be changed

#working with Tupple
def example():
    return 15,19

a,b = example() #sequence unpakcing-- a=15 and b=19

print(a)
print(b)

### Working with list now
x = [6,2,3,5,2,7,8,3]


print(x)
print(x[5])
x.append(12)
print(x)

x.insert(5,7) #inserting 7 at the 5th element
print(x)

x.remove(7)
print(x)

print(x.index(8))

print(x.count(3))

x.sort()
print(x)

y=['Spot','Cam','Jan','Dave']
print(y)

y.sort()
print(y)


y.reverse()
print(y)



