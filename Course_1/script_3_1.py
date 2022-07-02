"""
true=True
false=False
if(true):
    print('1 happened')
if(false):
    print('false happened')
else:
    print('2 happened')
if(not false):
    print('3 happened')
print('Boolean OoO = "not", then "and", then "or"')
print('1st indent = 2 spaces, 2nd = 4 spaces')
age=31
print('Your age is {}'.format(age))
if age>=35:
    print('You are old enough to be the President')
elif age>=30:
    print('You are old enough to be a Senator, but not the President')
else:
    print('You are not old enough to be the President or a Senator')
"""
"""
i=0
while i<=10:
    print('Count = {}'.format(i))
    i+=1
"""
i=range(10)  #remember that "10" is not included
for count in i:
    print('Count = {}'.format(count))
    if count==9:
        print(' ')
        
j=range(4,8)
for count in j:
    print('Count = {}'.format(count))
    if count==7:
        print(' ')

i=range(1,10,2)
for count in i:
    print('Count = {}'.format(count))
    if count==9:
        print(' ')



"""
animals = ['man','bear','pig']
for animal in animals:
    print(animal.upper())
"""    

