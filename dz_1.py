seconds = int(input("Введите время в секундах: "))

minutes_1 = (seconds // 60)
hour = minutes_1 // 60
minutes_2 = minutes_1 % 60
second = seconds % 60


print('seconds: {} minutes: {} hours: {}'.format(second , minutes_2 , hour))