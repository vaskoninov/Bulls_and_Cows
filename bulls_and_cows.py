import random


def main():

    while True:
        set_numbers = get_hidden_number()
        # print(set_numbers)
        number_tries = get_attempts()
        game(set_numbers, number_tries)

        if not new_game():
            print("Thank you for the game!")
            break


def game(set_numbers, number_tries):
    while True:

        if number_tries == 0:
            print("I am sorry, you don't have more tries!")
            break
        else:
            print(f"You have {number_tries} left!")

        user_guess = user_input("Please try to guess my 4 numbers!\n")

        winning_combination = check_numbers(set_numbers, user_guess)

        if winning_combination[0] == 4:
            print("You won!")
            print(f"The number was {''.join(set_numbers)}")
            break
        else:
            print("You got: ")
            print(f"Bulls: {winning_combination[0]}")
            print(f"Cows: {winning_combination[1]}")
            number_tries -= 1


def user_input(prompt):
    while True:
        try:
            get_numbers = input(prompt)
            list_numbers = [int(i) for i in list(get_numbers)]
        except ValueError:
            print("You need to enter valid integers!")
            continue
        if check_duplicates(list_numbers):
            return list_numbers
        else:
            print("You need to enter four different digits!")


def check_numbers(set_numbers, user_guess):
    bulls = 0
    cows = 0
    for i in range(len(user_guess)):
        if user_guess[i] in set_numbers:
            if user_guess[i] == set_numbers[i]:
                bulls += 1
            elif user_guess[i] != set_numbers[i]:
                cows += 1
    return (bulls, cows)


def get_hidden_number():
    while True:
        set_numbers = [random.randint(1, 9) for i in range(4)]
        if check_duplicates(set_numbers):
            return set_numbers


def get_attempts():
    number = int(input("How many times you will try to guess: "))
    return number


def new_game():
    answer = input('Do you want to play a new game?: (y)/(n)\n').lower()
    return True if answer == 'y' else False


def check_duplicates(numbers):
    return True if len(numbers) == len(set(numbers)) else False


if __name__ == "__main__":
    main()
