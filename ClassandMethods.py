'''
class testing:
    def getString(self):
        str_input = str(input('Enter a string : '))
        return str_input
    def printString(self,str_input):
        self.str_input = str_input
        print(str_input)

def test():
    A = testing()
    Name = A.getString()
    A.printString(Name)

test()
'''

class testing:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input('Enter a string : ')
    def printString(self):
        print('You have entered: ', self.s.upper())


A = testing()
A.getString()
A.printString()
