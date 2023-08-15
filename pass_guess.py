import string

def arrayOfLetters():
    alphabets = string.printable
    letters = ''
    for i in alphabets:
        letters += i
    return letters

def password_cracker(letters,password):
    your_pw = ''
    for i in password:
        print(i)
        print('Guessing pw: ',your_pw)
        for j in letters:
            print(j)
            if i == j:
                print('TRUE: ',j)
                your_pw += j
    return your_pw

def main():
    password = 'arina567474'
    print(password)
    letters = arrayOfLetters()
    print('Your password is: ',password_cracker(letters,password))
main()