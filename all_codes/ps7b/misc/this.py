'''
Jonathan Phouminh
106054641
Agrawal
Fall 2019 CU Boulder
CSCI 3104
Problem set 7b
edit: This is a continuation of ps1b code to now implement the same task of counting flips in nlogn time via mergesort.
'''
import math   #library to use pow()
import random  #library to use .shuffle()
flipcount = 0           # global variable to keep count of flips

def countFlip(n):
    a= list(range(1,n+1))  #creates list of size n from 1 . . . n
    size = len(a)
    random.shuffle(a)    #shuffles list
    if size == 0:  # edge case if the array is empty
        return 0
    flipCount = 0
    for i in range(size):
        for j in range(i+1, size):
            if a[i] > a[j] :
                flipCount+=1
    return flipCount



# merge the left and right sub arrays and
def merge(left,right):
    global flipcount
    leftIndex = 0   # keep a counter for current index that is being updated in the original array
    rightIndex = 0

    temp = []           # fill the array with the elements of both sub-arrays until one is exhausted, fill it in temp array then put it in orignal
    while (leftIndex < len(left) and rightIndex < len(right)):
        if (left[leftIndex] < right[rightIndex]): #element in left sub-array is larger
            temp.append(left[leftIndex])
            leftIndex+=1
        else:  # element in right sub-array is greater than or equal to the element in the left sub-array
            temp.append(right[rightIndex])
            rightIndex+=1
                # at this point one of the arrays should be exhausted so whichever one is just put the rest of elements into it
    while (leftIndex < len(left)):  # if it does this, then the right index isn't exhuasted
        temp.append(left[leftIndex])
        leftIndex+=1

    while (rightIndex < len(right)):
        temp.append(right[rightIndex])
        rightIndex+=1

    # everything in the temporary is now sorted

    flipcount+=1

    return temp

def mergesort(array):
    global flipcount
    # base case, when either the sub-array size is equal to zero or one
    if (len(array) == 1): # when array element size is one element we hit base case
        return array
    # recursively call to break down to the base case, s->mid and mid+1->e
    #mid = int((len(array))/2) # integer division, rounds down
    else:
        mid = int(len(array)//2)
        left = mergesort(array[:mid]) # left half
        right = mergesort(array[mid:])  # right half

        # if we come down to this line means we have finished breaking down and are going to
        # begin merging
        #arr = merge(left,right)
        return  merge(left,right)


def main():
    '''
            Arrays to test that the function is counting properly
    array1 = [1, 3, 5, 2, 4, 6]  # array given in the example, function expected to return 3 flips
    array2 = [1,2,3,8,7]  # function expected to return 1 flip
    array3 = [] # function should return 0
    '''
    arrayOfValulesToGenerate = []   #initiate an array of integers n where a[i] = 2^i , starting from i = 1
    flipCount = 0

    for i in range(1,21):
        arrayOfValulesToGenerate.append(pow(2,i))

    '''                                                     UNCOMMENT THIS BEFORE SUBMITTING
    #only compiling 2^i , where i >= 0 and i < 13
    print("COUNTING FLIPS IN QUADRATIC TIME")
    for i in range(len(0,12)):
        print("Element Count: ", arrayOfValulesToGenerate[i])
        flipCount = countFlip(arrayOfValulesToGenerate[i])
        print("Flip Count: " , flipCount)
    '''

    print("COUNTING FLIPS IN LOGARITHMIC TIME")
    for i in range(0,5):
        a = list(range(1,arrayOfValulesToGenerate[i]))      # creates list 1 . . . n
        random.shuffle(a)           # shuffles the list
        print("Element Count:", arrayOfValulesToGenerate[i])
        sorted_array = mergesort(a)
        print("FLIP COUNT: ", flipcount)
        print("==========")

main()

'''
    #testing the merge function to make sure it is merging properly
    array = [1,4,5,6]
    a1 = [1,2,3]
    a2 = [4,5,6]
    print("ORIGINAL ARRAY",a1+a2)
    print("MERGED ARRAYS",merge(a1,a2))
'''


'''
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                count+=1
'''
'''
        for i in range(len(left)): # counting flips for all the flips on the left sub-array
            for j in range(len(left)):
                if (left[i] > left[j]):
                    count+=1

        for j in range(len(right)):     # counting flips for all the flips on the right-subarray
            for k in range(len(right)):
                if (right[j] > right[k]):
                    count+=1
'''
