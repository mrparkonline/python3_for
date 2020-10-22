# Mod Inverse
'''
Given 0 < x < m, where x and m are integers:
the modular inverse of x is the unique integer n, 0<n<m,
such that the remainder on dividing x*n by m is 1.
Therefore, (x*n) % m is 1
'''

# input
num_x = int(input('Enter x: '))
num_m = int(input('Enter m: '))

# processing
n_found = False # this is going to track if we find a value
n = 0

for num_n in range(1, num_m):
    if (num_x * num_n) % num_m == 1:
        n_found = True
        n = num_n

if n_found:
    print(n)
else:
    print('No such integer exists.')
