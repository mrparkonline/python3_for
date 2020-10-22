# CCC 2003 S1 - Snakes and Ladders

# board has 3 snakes (from 54 to 19, from 90 to 48 and from 99 to 77) and 3 ladders (from 9 to 34, from 40 to 64 and from 67 to 86).

loop = True
location = 1 # this determines where the player is on the board

while loop:
    user_input = int(input('Enter a number from 2 to 12, 0 to quit: '))

    if user_input == 0:
        loop = False
        print('You Quit!')
    else:
        if location + user_input <= 100:
            location += user_input # updating the user's location

        if location == 54:
            location = 19
        elif location == 90:
            location = 48
        elif location == 99:
            location = 77
        elif location == 9:
            location = 34
        elif location == 40:
            location = 64
        elif location == 67:
            location = 86
        elif location == 100:
            loop = False

        print('You are now on square', location)

if location == 100:
    print('You Win!')
