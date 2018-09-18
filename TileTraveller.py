

stadsetning = 1.1
if stadsetning == 1.1:
    print('You can travel: (N)orth')
    direction = input('Direction: ')
    while direction != 'N' or 'n':
        print('Not valid direction')
        direction = input('Direction: ')
        if direction == 'N' or 'n':
            stadsetning = 1.1+0.1
            break

if stadsetning == 1.2:
    print('Tou can travel: (S)outh, (E)ast, (N)orth')
    direction = input('Direction: ')
    while direction == 'W' or 'w':
        print('Not valid direction')
        direction = input('Direction: ')
    else:
        if direction == 'N' or 'n':
            stadsetning = 1.2+0.1
        elif direction = == 'S' or 's':
            stadsetning = 1.2-0.1
        else direction == 'E':
            stadsetning = 1.2+1.0
        break

