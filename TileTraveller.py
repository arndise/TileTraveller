
stadsetning = 1.1
if stadsetning == 1.1:
    print('You can travel: (N)orth')
    direction = str(input('Direction: '))
    while direction == 'S' or 's' or 'E' or 'e' or 'W' or 'w':
        print('Not valid direction')
        direction = str(input('Direction: '))
    else direction == 'N' or 'n':
            stadsetning = 1.1+0.1

if stadsetning == 1.2:
    print('Tou can travel: (S)outh, (E)ast, (N)orth')
    direction = input('Direction: ')
    while direction == 'W' or 'w':
        print('Not valid direction')
        direction = input('Direction: ')
    else:
        if direction == 'N' or 'n':
            stadsetning = 1.2+0.1
        elif direction == 'S' or 's':
            stadsetning = 1.2-0.1
        elif direction == 'E' or 'e':
            stadsetning = 1.2+1.0

if stadsetning == 1.3:
    print('Tou can travel: (S)outh, (E)ast')
    direction = input('Direction: ')
    while direction == 'W' or 'w' or 'N' or 'n':
        print('Not valid direction')
        direction = input('Direction: ')
    else:
        if direction == 'S' or 's':
            stadsetning = 1.3-0.1
        elif direction == 'E' or 'e':
            stadsetning = 1.2-1.0
    

