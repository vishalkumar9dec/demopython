#Dictionary have key and value association
#All keys have to be unique
#mutable, not ordered

gradeDict = {'Kelly':89,'Vishal':70,'Nimmo':99,'Jack':95}


print(gradeDict['Nimmo'])

gradeDict['Nimmo'] = 98

print(gradeDict['Nimmo'])

gradeDict['Jessy']=92 ##adding new element in dictionary

print(gradeDict)

del gradeDict['Jessy'] ##Deleting element from dictionary
print(gradeDict)

#dictionary for multiple subjects
gradeDict2 = {'Kelly':[89,33],
              'Vishal':[70,65],
              'Nimmo':[99,92],
              'Jack':[95,83]}

print (gradeDict2)

print(gradeDict2['Jack'][0])

