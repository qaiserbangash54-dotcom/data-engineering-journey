#guess the number game project

Secret_number = 45
chance = 5 
while chance > 0:
    guess = int (input("guess the secret number:"))
    if guess == Secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        chance -= 1
        print(f"Wrong guess. You have {chance} chances left.")
    if guess < Secret_number:
        print("Hint: The secret number is higher.") 
    else:
        print("Hint: The secret number is lower.")