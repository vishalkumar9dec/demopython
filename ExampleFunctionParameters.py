'''def addition(num1, num2):
    answer = num1 + num2
    return answer

x = addition(5,6)
print(x)

#No limit on the number of parameters being passed


def website(font,background_color,font_size,font_color):
    print('font: ',font)
    print('BG:',background_color)
    print('Font_Size:',font_size)
    print('Font Color:',font_color)


website('TNR','white','11','Black')

#Giving wrong order of paramters
#website('TNR','white','Black','11')

# another way of doing'''

#default parameters
def website(font='TNR',
        font_size='11',
        font_color='White',
        background_color='Black'):
    print('font: ',font)
    print('BG:',background_color)
    print('Font_Size:',font_size)
    print('Font Color:',font_color)

#website() #calling function without giving paramters

#website(background_color='Grey')

website('TNR','Grey') # if only passing some parameters give the parameters in the correct order

