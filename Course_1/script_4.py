#Functions
"""
def my_first_function():
    print('You sucessfully ran my first function.')

def say_hi():
    print('Hi!')

#call the functions
my_first_function()
say_hi()
"""
"""
def say_hi(name):
    print('Hi {}!'.format(name))
say_hi('Jason')
"""

"""
def say_hi(name='there'):  #assigns a default value to "name" if no value is passed in
    print('Hi {}!'.format(name))
say_hi('Jason')
say_hi()
print(' ')

def say_hi(first, last):
    print('Hi {} {}!'.format(first,last))
say_hi('Jane', 'Doe')
say_hi(last='Doe',first='Jane') #defining them disregards the default order
"""

#def say_hi(first, last='Doe'):
#    """Say hello.
#    This is the help stuff aka DocString"""    #placing a comment here in triple quotes will display it in help
#    print('Hi {} {}!'.format(first,last))
#say_hi('Jane')
#say_hi('John', 'Coltrane')
#help(say_hi)


#def odd_or_even(number):
#    """Determine if a number is odd or even."""
#    if number %2==0:
#        return 'even'
#    else:
#        return 'odd'
#odd_or_even_string=odd_or_even(7)
#print(odd_or_even_string)

#Multi-layered functions
"""
def get_name():
    name=input('What is your name? ')
    return name
def say_name(name):
    print('Your name is {}.'.format(name))
def get_and_say_name():
    name=get_name()
    say_name(name)
"""
def get_name():
    first=input('What is your first name? ')
    last=input('What is your last name? ')
    name=[first,last]
    return name
def say_name(name):
    print('Your name is {0} {1}.'.format(name[0],name[1])) #index using []
def get_and_say_name():                             #() are for functions only!
    name=get_name()
    say_name(name)
get_and_say_name()


