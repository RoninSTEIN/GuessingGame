import random

def guessing(x):
    random_num=random.randint(1,x)
    guess = 0;
    score = 10 ;

    while guess != random_num:
        guess= int(input(f"C'mon Mate guess the number between 1 to {x}"))
        if guess < random_num and random_num - guess >=10:
            print("YOU GUESSED WRONG HEHEHE ... THE number is much bigger ")
            score = score -1
        elif guess < random_num and random_num - guess < 10:
            print("YOU GUESSED WRONG HEHEHE... THE number is bigger")
            score =score - 1
        elif guess > random_num and guess - random_num >= 10:
            print("YOU GUESSED WRONG HEHEHE... THE number is much smaller")
            score =score - 1        
        elif guess > random_num and guess - random_num < 10:
            print("YOU GUESSED WRONG HEHEHE... THE number is smaller")

            score =score - 1    

    print("NOICE YOU GUESSED IT RIGHT LET'S SEE YOUR SCORE THEN")
    print(score)

x = int(input("Enter the max number upto which you want to guess"))    
guessing(x)