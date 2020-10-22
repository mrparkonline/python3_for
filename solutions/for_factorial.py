num = int(input('Enter a value: '))

product = 1

for value in range(num, 0, -1):
    product *= value

print('Factorial of',num,'is', product)
