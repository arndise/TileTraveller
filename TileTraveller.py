
def north(status):
    status=round((status+0.1),1)
    return status

def south(status):
    status=round((status-0.1),1)
    return status

def east(status):
    status=round((status+1),1)
    return status

def west(status):
    status=round((status-1),1)
    return status

status=round(1.1, 2)

invalidInput = False
while 1.1 <= status <= 3.3:
    if status == 1.1 or status == 2.1:
        if invalidInput == False:
            print('You can travel: (N)orth.')
        direction = str(input('Direction: '))
        if direction == 'n' or direction == 'N':
            status = north(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True
            continue
    elif status == 3.1:
        print('Victory!')
        break
    elif status == 1.2:
        if invalidInput == False:
            print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = str(input('Direction: '))
        if direction == 'n' or direction == 'N':
            status = north(status)
            invalidInput=False
        elif direction == 'e' or direction == 'E':
            status = east(status)
            invalidInput=False
        elif direction == 's' or direction == 'S':
            status=south(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True 
            continue
    elif status == 1.3:
        if invalidInput == False:
            print('You can travel: (E)ast or (S)outh.')
        direction = str(input('Direction: '))
        if direction == 'e' or direction == 'E':
            status = east(status)
            invalidInput=False
        elif direction == 's' or direction == 'S':
            status=south(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True 
            continue
    elif status == 2.3:
        if invalidInput == False:
            print('You can travel: (E)ast or (W)est.')
        direction = str(input('Direction: '))
        if direction == 'w' or direction == 'W':
            status=west(status)
            invalidInput=False
        elif direction == 'e' or direction == 'E':
            status =east(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True 
            continue
    elif status == 3.2:
        if invalidInput == False:
            print('You can travel: (N)orth or (S)outh.')
        direction = str(input('Direction: '))
        if direction == 'n' or direction == 'N':
            status = north(status)
            invalidInput=False
        elif direction == 's' or direction == 'S':
            status=south(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True
            continue
    elif status == 3.3 or status == 2.2:
        if invalidInput == False:
            print('You can travel: (S)outh or (W)est.')
        direction = str(input('Direction: '))
        if direction == 's' or direction == 'S':
            status= south(status)
            invalidInput=False
        elif direction == 'w' or direction == 'W':
            status= west(status)
            invalidInput=False
        else:
            print('Not a valid direction!')
            invalidInput=True
            continue

