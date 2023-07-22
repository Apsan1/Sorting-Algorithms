import string
import random

def arrayOfLetters():
    alphabets = string.ascii_lowercase
    letters = []
    for i in alphabets:
        letters.append(i)
    return letters

def random_array(letters):
    n = len(letters)-1
    for i in range(n):
        random_index = random.randint(0,n)
        temp = letters.pop(random_index)
        letters.append(temp)
    return letters

def bubblesort(array):
    index_range = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_range):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
                print(array)
    return array
       
def main():
    letters  = arrayOfLetters()
    print(letters)
    new_array = random_array(letters)
    print(new_array)
    print(bubblesort(new_array))
main()