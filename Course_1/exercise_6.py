def get_person():
    person=input('Enter a name (press <enter> when done): ')
    return person

def get_fact(person):
    fact=input('Enter an interesting fact about {}: '.format(person))
    print('')
    return fact

interesting_facts={}  #initialize dictionary
blank=False

def create_facts():
    person=get_person()
    if len(person)==0:
        blank=True
    else:
        fact=get_fact(person)
        interesting_facts[person]=fact
    return person

while not blank:
    person=create_facts()
    if len(person)==0:
        blank=True

print('')
print('Here is your list')
print('-----------------')

for person, fact in interesting_facts.items():
    print('{}: {}'.format(person, fact))

print('')
print('Now change one of those facts')

correct=False

while not correct:
    to_change=input('About whom would you like to change a fact? ')
    if to_change in interesting_facts.keys():
        print('Okay, I\'ve found that person.')
        new_fact=input('What would you like to state about {}? '.format(to_change))
        print('')
        print('Okay, I\'ll get right on that...')
        interesting_facts[to_change]=new_fact
        print('Done!')
        print('Your new interesting fact about {} is {}'.format(to_change,interesting_facts[to_change]))
        correct=True
    else:
        print('')
        print('{} is not on your list.  Try again.'.format(to_change))
        print('')

print('')
print('Here is your new list')
print('---------------------')

for person, fact in interesting_facts.items():
    print('{}: {}'.format(person, fact))

print('')
print('Now let\'s add more people: ')

blank=False
while not blank:
    person=create_facts()
    if len(person)==0:
        blank=True

print('')
print('Here is your new list')
print('---------------------')

for person, fact in interesting_facts.items():
    print('{}: {}'.format(person, fact))
