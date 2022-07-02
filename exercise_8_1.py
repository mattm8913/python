file_lines=[]

with open('I:/Documents/Python Course/Scripts/files_input.txt') as file:
    for line in file:
        #file_lines[index]='{}'.format(line)  #works, if file_lines is initialized with 3 items, but should use something better
        file_lines.append(line)
print(file_lines)

        
with open('I:/Documents/Python Course/Scripts/files_output.txt','w') as file:
    index=0
    while index<len(file_lines):
        number=index+1
        #print('{}: {}'.format(number,file_lines[index]))
        file.write('{}: {}'.format(number,file_lines[index]))
        index+=1

print('')

with open('I:/Documents/Python Course/Scripts/files_output.txt') as file:
    for line in file:
        print(line.rstrip())
    
