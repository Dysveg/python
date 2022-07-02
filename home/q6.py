def new_list(list):
    l = []
    while len(list) > 0:
        if list.count(list[0]) > 1:
            a = list[0]
            count = list.count(list[0])
            l.append(count)
            for j in range(count):
                if a in list:
                    list.remove(a)
        else:
            l.append(list[0])
            list.remove(list[0])
    return l


l = [int(i) for i in input('Enter a list of numbers (0-9): ').split()]
print(new_list(l))