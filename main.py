#question no.1
import random


def main():
    try:
        num_dice = int(input("How many dice do you want to roll? "))
        if num_dice <= 0:
            print("Please enter a positive number of dice to roll.")
            return

        total_sum = 0
        for _ in range(num_dice):
            roll = random.randint(1, 6)
            print(f"Rolled: {roll}")
            total_sum += roll

        print(f"Sum of the numbers rolled: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter a valid number of dice.")


if __name__ == "__main__":
    main()

#question no.2
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if len(numbers) < 5:
    print("You need to enter at least 5 numbers.")
else:

    numbers.sort(reverse=True)

    print("The five greatest numbers sorted in descending order are:")
    for i in range(5):
        print(numbers[i])

#question no. 3
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:

        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


try:
    user_input = int(input("Enter an integer: "))

    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#question no. 4
cities = []

for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("City names:")
for city in cities:
    print(city)
