n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

if n1>n2 and n1>n3:
    print(n1, 'is Largest')
    if n2>n3:
        print(n3, 'is smallest')
    else:
        print(n2, 'is smallest')

elif n2>n1 and n2>n3:
    print(n2, 'is Largest')
    if n1>n3:
        print(n3, 'is smallest')
    else:
        print(n1, 'is smallest')

elif n3>n2 and n3>n1:
    print(n3, 'is Largest')
    if n2>n1:
        print(n1, 'is smallest')
    else:
        print(n2, 'is smallest')

else:
    print('all numbers are same')
