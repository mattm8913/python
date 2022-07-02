to_do_list=[]
index=0
task='Initialized'
while task!='':
    print('Enter a task for your to-do list (press <enter> when done): ')
    task=input()
    if task!='':
        to_do_list.append(task)
        print('Task added.')
"""
print('Here is your To-Do List:')
print('------------------------')
for index in range(0,len(to_do_list)):
    print('{}'.format(to_do_list[index]))
"""

print('Here is your To-Do List:')
print('------------------------')
for task in to_do_list:
    print(task)
