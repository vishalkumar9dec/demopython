StudentGrades = {
    'Ivan': [4.32, 3, 2],
    'Martin': [3.45, 5, 6],
    'Stoyan': [2, 5.67, 4],
    'Vladimir': [5.63, 4.67, 6]
}

avgDict = {}
for k,v in StudentGrades.items():
    # v is the list of grades for student k
    avgDict[k] = sum(v)/ float(len(v))

print(avgDict)

'''
from statistics import mean

StudentGrades = {
    'Ivan': [4.32, 3, 2],
    'Martin': [3.45, 5, 6],
    'Stoyan': [2, 5.67, 4],
    'Vladimir': [5.63, 4.67, 6]
}

for st,vals in StudentGrades.items():
    print("Average for {} is {}".format(st,mean(vals)))
'''
