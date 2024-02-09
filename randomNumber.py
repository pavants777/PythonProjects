import random as np

def guess(x) :
    random_number = np.randint(1, x);
    guess = 0
    while guess != random_number: 
          guess = int(input(f'Enter a Number between 1 to {x} :'))
          if guess > random_number : 
              print("Your Guess is Incorrect ! ... Enter Too Lowww")
          else : 
              print("Your Guess is Incorrect ! ... Enter Too High")
    print("Your Guess is Correct ! ....Yay! Congrats")
    
    
guess(50)
    