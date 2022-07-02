def list_check(num):
    for i in num:
        if not isinstance(i,int):
            raise ValueError('Objects of the list have to be type int!')
        elif not 1 <= i <= 100:
            raise ValueError('Objects of the list have to be between 1 and 100!')

print(list_check([1,2,3,'h']))
