def high_and_low(numbers):
    highest=max(numbers)
    lowest=min(numbers)
    return[highest,lowest]

lottery_numbers=[16,4,42,15,23,8]
[highest,lowest]=high_and_low(lottery_numbers)
print('Highest = {}'.format(highest))
print('Lowest = {}'.format(lowest))
[highest,lowest]=[1,50]
print('New Highest = {}'.format(highest))
print('New Lowest = {}'.format(lowest))

contact=[('Jason','555-0123'),('Carl','555-0987')]
for (name,phone) in contact:
    print("{}'s phone number is {}".format(name, phone))

contacts=[['Jason','555-0123'],['Carl','555-0987']]
for (name,phone) in contacts:
    print("{}'s phone number is {}".format(name, phone))
