

stadsetning = 1.1
if stadsetning == 1.1:
    print('You can travel: (N)orth)')
    direction = input('Direction: ')
    if direction != 'N':
        print('Not valid direction')
        direction = input('Direction: ')