import random
def random_list():
    randomlist = []
    for i in range(0,5):
        n = random.randint(1,30)
        randomlist.append(n)
    return randomlist

def bubblesort(array):
    index_range = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_range):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
                print(array,'\n\n')
    return array
       
def main():
    array = random_list()
    print(array,'\n\n')
    print(bubblesort(array))
main()