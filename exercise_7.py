def get_airport():
    airport=input('Airport? ')
    return airport

def get_code():
    code = input('Code? ')
    return code

blank=False
index=0
airports=[]

while not blank:
    print('Hit <enter> when done.')
    airport=get_airport()
    if len(airport)==0:
        blank=True
    else:
        code=get_code()
        airports.append((airport,code))
        index += 1

print('')
print('You finished creating your list')
print('')
print('Here is your list:')
print('------------------')

for (airport,code) in airports:
    print('The code for {} is {}.'.format(airport,code))
    
    
