import random


class GuessNumber:
    __random_number = 0
    def __init__(self,l,h):
        self.low = l;self.high = h
    
    def genRandNum(self):
        self.__random_number = random.randint(self.low,self.high)
        print(f"Actual Number is {self.__random_number}")

    def numberGuess(self,guess_Num):
        guess = 0
        while guess != self.__random_number:
            # guess = int(input("enter a number to match with random number-> "))
            guess = guess_Num
            if(guess > self.__random_number):
                print("Too high")
                return 'h'
            elif guess < self.__random_number:
                print("too low")
                return 'l'
        print(f"You are correct {guess}")
        return 'c'
    



def computerGuess(x):
    low = 1;high =x
    feedback = ''
    genRand = GuessNumber(1,10)
    genRand.genRandNum()

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        # feedback = input(f"If correct type 'c', if high type 'h', if low type 'l'").lower()
        feedback = genRand.numberGuess(guess)
        if(feedback == 'l'):
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
            
    print(f"You are correct 2 ## {guess}")        
    

computerGuess(10)    