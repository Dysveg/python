def func(text):
    n = [int(i) for i in text]
    n = sum(n)
    text.append(str(n))
    return text
k = list(input())
print(''.join(func(k)))