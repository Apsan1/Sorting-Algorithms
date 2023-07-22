from random import randint,shuffle

def  create_array(size=10,max=50):
    return[randint(0,max) for _ in range(size)]

def is_sorted(a):
    for i in range(1,len(a)):
        if a[i]< a[i-1]: return False
    return True

def bogo_sort(a):
    count = 0
    while not is_sorted(a):
        shuffle(a)
        print(a)
        count+=1
    return count,a

a = create_array(8,50)
sorted_a = a
print('Your array is: ',a)
ct, s = bogo_sort(a)
print(s)
print('Your array was sorted: ',sorted_a,' after ',ct,' tries.')