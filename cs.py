import string
import random
'''
 cs go bomb planter
'''
def bomb_planter():
    bomb = ''
    for i in range(7):
        bomb += str(random.randint(0,9))
    return bomb

def arrayOfLetters():
    zero2nine = string.digits
    numbers = ''
    for i in zero2nine:
        numbers += i
    return numbers

def password_cracker(letters,password):
    your_pw = ''
    for i in password:
        
        for j in letters:
            print(i,j)
            if i == j:
                print(True)
                your_pw += j
    return your_pw

def main():
    bomb = bomb_planter()
    letters = arrayOfLetters()
    print('Your plant code was: ',password_cracker(letters,bomb))
    print('Bomb has been defused!')
main()