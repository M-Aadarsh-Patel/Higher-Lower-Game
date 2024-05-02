import random
from game_data import data
from art import logo, vs

def Info_to_user(celebrety1, celebrety2):
    print(f"Compare A: {celebrety1['name']}, a {celebrety1['description']} from {celebrety1['country']}")
    print(vs)
    print(f"Against B: {celebrety2['name']}, a {celebrety2['description']} from {celebrety2['country']}")

def game():
    print(logo)

    score = 0

    A = random.choice(data)
    index_of_A = data.index(A)
    print(index_of_A)
    del data[index_of_A]
    B = random.choice(data)

    while True:

        Info_to_user(celebrety1=A, celebrety2=B)
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

                A = B
                B = random.choice(data)

            else:
                print(f"That's the wrong guess, You had a score of {score}")
                break

game()