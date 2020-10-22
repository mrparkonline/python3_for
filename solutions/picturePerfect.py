# CCC 2003 J2 - Picture Perfect

user_input = -1
while user_input != 0:
    user_input = int(input('Enter the number of pictures: '))

    if user_input != 0:
        upper_limit = int(user_input ** 0.5) + 1 # sqrt of user_input
        # so that we may create squares

        min_perimeter = 0
        side1_answer = 0
        side2_answer = 0

        for dimension in range(1, upper_limit):
            if user_input % dimension == 0:
                side1 = dimension
                side2 = user_input // dimension
                perimeter = 2*side1 + 2*side2
                #print('Current perimeter:', perimeter)
                #print('Dimension:', side1, 'x', side2)

                if min_perimeter != 0 and perimeter < min_perimeter:
                    min_perimeter = perimeter
                    side1_answer = side1
                    side2_answer = side2
                elif min_perimeter == 0:
                    min_perimeter = perimeter
                    side1_answer = side1
                    side2_answer = side2
        # end of for
        print('Minimum perimeter is',min_perimeter, 'with dimensions', side1_answer, 'x', side2_answer)
