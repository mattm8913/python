

def main():
    number_list=[0]
    index=1
 
    print(number_list[index-1])
    print('')
    """
    print(number_list[index-1]+2)
    print((number_list[index-1]+2)**3)
    """
    while index<20000:
        #print(str((number_list[index-1]+2)**3))
        number=(number_list[index-1]+2)
        #print(number)
        number_list.append(number)
        print(number_list[index])
        print('')
        index+=1

if __name__=='__main__':
    main()

"""
number=(number_list[index-1]+2)^3
number_list.append(number)
print(number_list[index])
index+=1 
"""
