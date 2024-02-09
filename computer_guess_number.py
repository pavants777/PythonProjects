import random 

def computer_guess(x) : 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' : 
        guess = random.randint(low, high)
        print(f'Computer Guessed Number = {guess}')
        feedback = str(input("Enter\n (L) if Too Low \n (H) if Too High \n (C) if is Correct : ").lower())
        if feedback == 'l' : 
           low = guess+1
        elif feedback == 'h' : 
            high = guess-1 
    print(f'Yay ! Computer Guess Your Correct Number {guess}')
    
computer_guess(10)