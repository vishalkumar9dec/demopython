#Python project for student grades

import statistics as s

print('Login with admin credentials to access Grade Central:....')
username = input('Username: ')

studentsGrade = {'Vishal':[45,87,98],
                 'Prodipto': [65,76,87],
                 'Pallav': [87,76,76]}

def firstMenu():
    print('1. Enter Grades.')
    print('2. Remove student.')
    print('3. Student Average Grades.')
    print('4. Exit')
    choice=int(input('Enter your choice : '))
    #var_choice = int(choice)
    if choice >= 4 :
        print('Invalid Selection...')
    else:
        return choice


def gradeOperations(choice):
    if choice == 1:    
        addStudent()
    elif choice == 2:
        removeStudent()
    elif choice == 3:
        studentAverage()
    else:
        exit()


def addStudent():
    print('Enter the below details:')
    sName = input('Student Name : ')
    Grade = input('Grade : ')

    if sName in studentsGrade:
        studentsGrade[sName].append(float(Grade))
        print('Student grade added successfully. Updated details as below:')
        print(studentsGrade)
    else:
        print('Student not found. Please give an existing user')

def removeStudent():
    sNametoDelete = input('Enter the name of the student to be deleted: ')
    print('Are you sure to delete?')
    user_Choice = int(input('enter 1 for yes or 2 for no :'))
    if user_Choice == 1:
        del studentsGrade[sNametoDelete]
        print('Student deleted successfully. Updated details as below:')
        print(studentsGrade)
    
def studentAverage():
    for eachStudent in studentsGrade:
        gradeList = studentsGrade[eachStudent]
        print(gradeList)
        avgGrade = s.mean(gradeList)

        print(eachStudent,'has an average grade of:',avgGrade)
    
        

if username == 'admin':
    password = input('Password: ')
    if password == '1234':
        print('Welcome to Grade Central !')
        user_choice = firstMenu()
        gradeOperations(user_choice)
else:
    print('User not found..')
    print('Please login with admin credentials')




