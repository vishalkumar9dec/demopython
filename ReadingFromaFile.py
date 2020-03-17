readme = open('exampleWrite.txt','r').read()
print(readme)

splitMe = readme.split('\n')

#print(splitMe[1])  #This splits the file and prints the output in a List

readMe = open('exampleWrite.txt','r').readlines() #This directly gives the output in list
print(readMe)
