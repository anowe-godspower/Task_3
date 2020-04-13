first   = 1500
second  = 2701

for number in range(first, second):
    if ((number % 7 == 0) and (number % 5 == 0)):
        print(number)