# q6a digit sum

# input
number = int(input('Enter a number: '))

total = 0

for str_num in str(number):
    print(str_num, type(str_num))
    total += int(str_num)

print('Digit Sum:', total)


# 6b. Greatest Digit Sum
'''
From 1 to 1000, determine which number has the greatest digit sum.

Example:

From 10 to 20, 19 has the greatest digit sum of 10
'''

answer = 0 # the number that generated the largest sum
the_sum = 0 # the digit sum

for num in range(1,1000):
    # digit sum calculation
    current = 0 # we need to num's digit sum

    for digit in str(num):
        current += int(digit)
    # digit sum ended

    # compare the previous largest digit sum
    if current > the_sum:
        answer = num
        the_sum = current
# end of for

print(answer, 'has the greatest digit sum of', the_sum)

# q6c digit sum until we have a single digit

# input
number = int(input('Enter a number:'))

# processing
counter = 0 # counting how many times I have done the digit sum
str_num = str(number)

while len(str_num) != 1:
    total = 0
    for digit in str_num:
        total += int(digit)
    # end of for

    counter += 1 # increase my counter!
    str_num = str(total)
# end of while

# output
print(number, 'required', counter, 'digit sums to become a single digit.')
