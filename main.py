import random
from game_data import data
from art import logo, vs


def game():
    print(logo)

    A = random.choice(data)
    B = random.choice(data)

    score = 0

    while True:
        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
        print(f"{A['follower_count']}")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")
        print(f"{B['follower_count']}")

        guess = input("Who has more followers A or B: ")

        if guess.lower() == 'a':
            if A['follower_count'] > B['follower_count']:
                print("You guessed it right, You won!")
                score += 1

                B = random.choice(data)
            
            else:
                print(f"That's the wrong guess, You had a score of {score}")
                break

        elif guess.lower() == 'b':
            if B['follower_count'] > A['follower_count']:
                print("You guessed it right, You won")
                score += 1

                A = random.choice(data)

            else:
                print(f"That's the wrong guess, You had a score of {score}")
                break

game()