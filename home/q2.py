def not_devision(n,d):
    numbers = []
    [numbers.append(n[i]) for i in range(len(n)) if n[i]  % d != 0]
    return l

d = int(input('Enter a number: '))
n = [int(i) for i in input('Enter a list of numbers: ').split()]
print(not_devision(n,d))