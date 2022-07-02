def avr(num):
    total = sum(num)
    result = total / len(num)
    return result
q = int(input('Enter a limiter: '))
numbers = [int(input('Enter a number: ')) for i in range(q)]
print('Average of numbers: ',avr(numbers))





