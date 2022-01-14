import random

num = random.randint(1,100)
print(num)
guesses = [0]

while True:
    guess = int(input('Enter your guess: '))
    if 1 > guess or guess > 100:
        print('Out of Bounds!')
        continue

    if guess == num:
        print(f'You guessed the number in {len(guesses)} turns')
        break

    guesses.append(guess)
    # print(guesses)

    if guesses[-2]:
        if abs(num-guess) < abs(guesses[-2]-num):
            print('Warmer!')
        else:
            print('Colder!')
    else:
        if abs(num-guess) <= 10:
            print('Warm!')
        else:
            print('Cold!')
