import random

count = 0
test_number = random.randrange(1, 20)
my_name = input("Hello! What's your name?\n")
print(f"Well, {my_name}, I am thinking of a number between 1 and 20")
my_number = int(input("Take a guess.\n"))


while (my_number!=test_number):
    print("\nYour guess is too low.")
    my_number = int(input("Take a guess.\n"))
    count = count + 1


print(f"\nGood job, {my_name}! You guessed my number in {count+1} guesses!")