n = 20
number_of_guess = 1

while(number_of_guess <= 9):
    a = int(input("Guess a number\n"))
    if a > n:
        number_of_guess = number_of_guess + 1
        print("choose a smaller number")
    elif a < n:
        number_of_guess = number_of_guess + 1
        print("choose a bigger number")
    else:
        print("you have won")
        break
if number_of_guess >= 9:
    print("game over")
