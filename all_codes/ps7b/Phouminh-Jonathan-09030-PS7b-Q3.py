
def hindex(array):
    n = len(array)
    count = 1
    index = 1
    NsubH = n - index
    array.sort(reverse = True) # sorts the array in descending order
    for i in range(1,n):
        if (array[i] <= array[i-1] and index <= NsubH):
            index += 1
            NsubH -= 1
    for i in range(index):
        count = count + 1

    print("h index: ", count)


def main():
    '''
        TEST ARRAYS
        arr =[6, 5, 3, 1, 0]
        H_index(arr)
        arr2 = [86, 75, 63, 11, 3]
        H_index(arr2)
    '''
    temp = []
    n = int(input("INPUT ARRAY SIZE: "))
    for i in range(n):
        x = int(input("input value: "))
        temp.append(x)

    hindex(temp)

main()

# go back figure out how to do it recursively
