# Iteration Review
# Q3 - Perfect Numbers

total_sum = 0

for num in range(1, 10000):

    # I need to determine if num is a perfect number
    current_divisor_sum = 0

    for divisor in range(1, num):
        if num % divisor == 0:
            # divisor is a proper divisor
            current_divisor_sum += divisor
    # end of finding the proper divisor

    if current_divisor_sum == num:
        # we have a perfect number
        print(num, 'is a perfect number.')
        total_sum += current_divisor_sum
    # end of checking if num is a perfect number
# end of for loop

print('The total sum of all perfect numbers from 1 to 10000 is:', total_sum)
