
stadsetning = 1.1

while stadsetning != 3.1:

    if stadsetning == 1.1:
        print('You can travel: (N)orth.')
        direction = input('Direction: ')
        while direction == 'S' :#or direction == 's' or direction =='W' or direction =='w' or direction == 'E' or direction =='e':
            print('Not a valid direction!')
            direction = input('Direction: ')
        stadsetning = 1.1 + 0.1
    
    if stadsetning == 1.2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = input('Direction: ')
        while direction == 'W' or direction == 'w':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'N' or direction =='n':
            stadsetning = 1.2 + 0.1
        elif direction == 'E' or direction =='e':
            stadsetning = 1.2 + 1.0 
        elif direction == 'S' or direction =='s':
            stadsetning = 1.2 - 0.1
    
    if stadsetning == 1.3:
        print('You can travel: (E)ast or (S)outh.')
        direction = input('Direction: ')
        while direction == 'W' or direction == 'w' or direction == 'N' or direction =='n':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'E' or direction =='e':
            stadsetning = 1.3 + 1.0 
        elif direction == 'S' or direction =='s':
            stadsetning = 1.3 - 0.1

    if stadsetning == 2.2:
        print('You can travel: (W)est or (S)outh.')
        direction = input('Direction: ')
        while direction == 'E' or direction == 'e' or direction =='N' or direction == 'n':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'W' or direction =='w':
            stadsetning = 2.2 - 1.0
        elif direction == 'S' or direction =='s':
            stadsetning = 2.2 - 0.1

    if stadsetning == 2.1:
        print('You can travel: (N)orth')
        direction = input('Direction: ')
        while direction != 'N' or direction != 'n':
            print('Not a valid direction!')
            direction = input('Direction: ')
        stadsetning = 2.1 + 0.1
    
    if stadsetning == 2.3:
        print('You can travel: (W)est or (E)ast.')
        direction = input('Direction: ')
        while direction == 'N' or direction == 'n' or direction =='S' or direction == 's':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'W' or direction =='w':
            stadsetning = 2.3 - 1.0
        elif direction == 'E' or direction =='e':
            stadsetning = 2.2 + 1.0       
    
    if stadsetning == 3.3:
        print('You can travel: (W)est or (S)outh.')
        direction = input('Direction: ')
        while direction == 'E' or direction == 'e' or direction =='N' or direction == 'n':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'W' or direction =='w':
            stadsetning = 3.3 - 1.0
        elif direction == 'S' or direction =='s':
            stadsetning = 3.3 - 0.1
    
    if stadsetning == 3.2:
        print('You can travel: (N)orth or (S)outh.')
        direction = input('Direction: ')
        while direction == 'W' or direction == 'w' or direction =='E' or direction == 'e':
            print('Not a valid direction!')
            direction = input('Direction: ')
        if direction == 'N' or direction =='n':
            stadsetning = 3.2 + 1.0
        elif direction == 'S' or direction =='s':
            stadsetning = 3.2 - 0.1

