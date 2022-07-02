animals_sorted_list=['']
animals_list=[]

with open('I:/Documents/Python Course/Scripts/animals.txt') as animals:
    for line in animals:
        animals_list.append(line)

print(animals_list)

animals_sorted_list=sorted(animals_list)

with open('I:/Documents/Python Course/Scripts/animals-sorted.txt','w') as animals_sorted:
    index=0
    while index<len(animals_sorted_list):
        animals_sorted.write(animals_sorted_list[index])
        index+=1

print(animals_sorted_list)

with open('I:/Documents/Python Course/Scripts/animals-sorted.txt') as animals_sorted:
    for line in animals_sorted:
        print(line.rstrip())
    
