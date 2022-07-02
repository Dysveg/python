import random

print('if you wanna stop the game enter "Stop".')
i,l,ls = 1,[],[]
flag = True
while flag:
    ls.append(random.randint(1, 9))
    num = input(f'Enter a {i} number 0-9: ')

    if num == 'Stop':
        break

    if int(num) > 9:
        print('Error, Enter a number between 0 and 9!')
        continue

    l.append(int(num))
    i += 1

    if len(l) < 3:
        continue

    if ls == l:
        print('You won!')
        flag = False

    else:
        print('You lost!','Try again',sep = '\n')
        ls.clear()
        l.clear()
        i = 1
        continue




