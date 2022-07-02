def cat_say(text):
    var=text
    #var='Pet me and I will purr.'
    space=' '
    u_line='_'
    dash='-'
    indent=10
    length=len(var)
    print('{0}{1}'.format(space*(indent+2),u_line*length))
    print('{0}< {1} >'.format(space*indent,var))
    print('{0}{1}'.format(space*(indent+2),dash*length))
    print('{}/'.format(space*indent))
    print(' /\_/\   /')
    print('( o.o )')
    print(' > ^ <')

def main():
    text=input('What does the cat say? ')
    cat_say(text)

if __name__ == '__main__':
    main()
    
