distance=input('How far would you like to travel in miles?  ')
dist=int(distance)
if dist<3:
    print('I suggest walking to your destination')
elif dist<300:
    print('I suggest driving to your destination')
else:
    print('I suggest flying to your destination')
