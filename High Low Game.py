import random
user_num = 1
game_num = random.randint(1, 100)
tries = 5

while user_num != game_num and tries > 0:
    user_num = int(input('Please enter number between 1 and 100, you have ' + str(tries) + ' tries left'))
    if user_num > game_num:
        print('This is too high')
        tries = tries - 1
        continue
    elif user_num < game_num:
        print('Too low')
        tries = tries - 1
        continue
    elif user_num == game_num:
        print('Nice!')
        continue

if user_num == game_num:
    print('You win, try again!')

if user_num != game_num:
    print('You lose, the number was ' + str(game_num) + ' try again sucker')
