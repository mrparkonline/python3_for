# Q4 Factor Finder using a for loop

num = int(input('Enter a value: '))

for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(divisor, 'is a factor of', num)
