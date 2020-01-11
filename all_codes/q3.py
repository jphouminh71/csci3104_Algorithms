import random
def p2_greedy(array,p2):
    last = len(array)-1
    if array[0] < array[last]:
        p2.append(array[0])
        del array[0]
        print("p2 array: ",array)
    else:
        p2.append(array[last])
        del array[last]
        print("p2 array")

# goal of this turn is to look one turn ahead
def p1_opt(array,p1):
    # these variables will be used as a simulation to see what the opponent would end up with
    # we take the value that is minimal
    first_choice_sum = 0  # the best case if we take the last element
    second_choice_sum = 0   # the best case possible to get the first element
    lastIndex = len(array)-1
    startIndex = 0
    if (len(array) == 2):
        if array[0] < array[1]:
            p1.append(array[0])
            del array[0]
        else:
            p1.append(array[1])
            del[array[1]]
        return
    if(array[lastIndex-1] < array[startIndex]): # this means that the opponenet will take the value that is -1 of the last index
        first_choice_sum = array[lastIndex] + min(array[startIndex],array[lastIndex-2]) # we do minus two because the computer would have grabbed lastI-1
    else:
        first_choice_sum = array[lastIndex] + min(array[startIndex+1], array[lastIndex])
    if(array[lastIndex] < array[startIndex+1]): # this will be the outcome one move ahead by picking the first index
        second_choice_sum = array[startIndex] + min(array[startIndex+1],array[lastIndex-1]) # we do plus two because the computer would have grabbed startIndex-1
    else:
        second_choice_sum = array[startIndex] + min(array[startIndex+2], array[lastIndex])

    if first_choice_sum < second_choice_sum:
        p1.append(array[lastIndex])
        #array.remove(lastIndex)
        del array[lastIndex]

    else:
        p1.append(array[startIndex])
        #array.remove(lastIndex)
        del array[startIndex]

    return


# function will just play the game entirely
def epic(array,p1,p2):
    print(p1)
    print(p2)
    print("------------")
    # player one will always go first
    size = len(array)
    while(size > 0):
        #print("player1's turn")
        #print("Array Before P1 turn: ", array)
        p1_opt(array,p1)        # player 1 turn
        print("P1 CARDS: ", p1)
        #print("player2's turn")
        #print("Array Before P2 turn: ", array)
        p2_greedy(array,p2)     # player 2 turn
        #print("P2 CARDS: ", p2)
        #print("-------")
        size = size - 2
    '''         wrong, TA said cant do this because it results in un-optimal
    # if we come out here it means that we hit the last 2 elements so we will just make p1 take the minimum element and p2 take the last element
    min_value = min(array[0],array[1])
    p1.append(min_value)
    array.remove(min_value)
    p2.append(array[0])
    array.remove(array[0])

    realized that could possibly not always optimal solution because we don't consider the previous cards that were picked.
    '''
    return
def main():
    # player loses if the cards are very near sorted in ascending order
    p1 = []
    p2 = []
    #test1 = [ 8, 7, 6, 11, 5, 4, 3, 1]
    test2 = [4,2,6,5]
    test3 = [35,83,47,37,90,10,13,2,96,50,93,36,64,95]
    test4 = [9,8,10,9]
    anton = [16, 37, 14, 40, 23, 2, 29, 8, 1, 36, 27, 25, 17, 10, 19, 12, 22, 6, 15, 4, 30, 18, 33, 13, 32, 20, 11, 34, 24, 9, 28, 3, 7, 35, 39, 5, 38, 26, 31, 21]
    temp = []
    for i in range(100):
        temp.append(i)
    random.shuffle(temp)
    epic(anton,p1,p2)
    print("PLAYER 1 CARDS", p1)
    print("PLAYER 2 CARDS", p2)
    print("P1 SCORE: " ,sum(p1))
    print("P2 SCORE: " ,sum(p2))
    temp = []
    return
main()
