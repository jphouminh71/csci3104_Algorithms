import math
import random

flipcount = 0           # global variable to keep count of flips

# merge the left and right sub arrays and
def merge(left,right):
    global flipcount
    # keep a counter for current index that is being updated in the original array
    leftIndex = 0
    rightIndex = 0
    # fill the array with the elements of both sub-arrays until one is exhausted, fill it in temp array then put it in orignal
    temp = []
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

    a = [1,3,5,2,4,6]  #flip count should be 3
    numberElements = 0  # will hold the number of elements that current iteration will hold
    numberElements = int(input("Enter element count: "))

    '''
    for i in range(numberElements):
        x = input("Enter number: ")
        a.append(int(x))
    '''
    print("INPUTTED ARRAY:", a)
    sorted_array = mergesort(a)
    print("OUTPUT ARRAY:", sorted_array)
    print("FLIP COUNT",flipcount)


main()

'''
        Code to test to make sure merge is working correctly

        a1 = [1,3,4,5,4]
        a2 = [5,7,8]
        print(merge(a1,a2))

'''

'''
        doesn't work, losing start and end indexs
    mid = (s+e)//2
    i = s  # start index for the 'left' sub-array
    j = mid+1  #start index for the 'right' sub-array
    k = s  #index for the current index of the array we will use to copy from
    temp = []
    while ( i <= mid and j <= e):
        if (array[i] < array[j]):
            #temp[k+=1] = array[i+=1]
            temp.append(array[i])
            k = k + 1
            i = i + 1
        else:
            #temp[k=+1] = array[j=+1]
            temp.append(array[j])
            k = k + 1
            j = j + 1
    # copy all elements that are from either array that is still empty
    while (i<=mid):
        #temp[k] = array[i]
        temp.append(array[i])
        i = i + 1
    while (j<=e):
        temp.append(array[j])
        j = j + 1
'''
'''
Function takes in the array, the startIndex, and the endIndex,
going to recursively call itself
'''
