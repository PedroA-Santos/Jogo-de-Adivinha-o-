import random 

def guess (x):
    random_number = random.randint (1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f"Adivinhe um número entre 1 e {x}: "))
        if guess < random_number:
            print ("Desculpe, adivinhe novamente, número muito baixo. ")
        elif guess > random_number:
            print ("Desculpe, adivinhe novamnete, número muito alto. ")

            
        print (f"Sim parabéns, você adivinhou o número {random_number} com sucesso. ")

        
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess= random.randint(low, high)
        else:
            guess = low #também pode ser alto b/c baixo = alto
        feedback = input(f"o número {guess} é, Muito alto? [A], muito baixo? [B], correto? [C] ").lower()
        if feedback == "a":
            high = guess - 1
        elif feedback == "b":
                low = guess + 1

    
    print(f"Sim, o computador adivinhou seu número, {guess} , corretamente! ")


computer_guess(1000)
    
                     


