from art import logo, vs
from game_data import data
import random
import os

# Display art
print(logo)


# Return formatted shape of an account
def format_account(account):
    acount_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{acount_name}, a {account_description} from {account_country} "


def check(guess, a_followers_account, b_followers_account):
    ### Check the answer anf if it is right return true ###
    if a_followers_account > b_followers_account:
        return guess == "a"
    else:
        return guess == "b"


score = 0
is_game_continue = True
account_b = random.choice(data)


# Make game repeatable
while is_game_continue:

    # Choose two random data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_account(account_a)}")
    print(vs)
    print(f"Against B : {format_account(account_b)}")

    # Ask for user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #  Compare user guess with random data
    ## Find the amount of followers
    a_followers_account = account_a["follower_count"]
    b_followers_account = account_b["follower_count"]

    is_correct = check(guess, a_followers_account, b_followers_account)

    os.system("cls||clear")

    ## If it is correct score data
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        is_game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

    # Change b position with a position
