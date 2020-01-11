import timeit

'''
    Equation to find pell number:
            Pn = 2Pn-1 + Pn-2
            P(1) = 1
            P(0) =
    Function will implement Pell Number calculation with top down approach
    n: pell number to calculate

    base case p(1) = 1
    base case p(0) = 1
'''
def pellNum(n):
    if (n == 1 or n == 0):          # once base case has been hit return
        return 1
    else:
        return 2*pellNum(n-1) + pellNum(n-2)


'''
    memoized version, small changes, need to add a conditional that checks whether or not a value has been calculated and
    if that has already been calculated then return that value
    - save each result as it is calculated
'''
def pellNum_memo(array,n):
    if n == 1 or n == 0:
        array[n] = 1
        #print("VALUE", array[n])
        return 1
    if array[n] is not None:
        return array[n]
    else:
        array[n] = (2*pellNum_memo(array,n-1) + pellNum_memo(array,n-2))    # save the value that was just calculated for this n
        #print("VALUE" , array[n])
    return array[n]


def pennNum_bottomUp(n):
    memo = []
    if n == 1 or n == 2:  # base cases
        return 1
    if n == 3:
        return 3          # trivially true
    memo.append(1)      # this allows us to actually perform bottom up
    memo.append(1)

    for i in range(2,n+1):    # essentially here, we will just build up pell num from our base cases
        memo.append((2*memo[i-1] + memo[i-2]))   # keep populating the array of values to get the next pell numbers
    return memo[n]

def pennNum_bottomUp_Efficient(n):
    if n == 1 or n == 0:
        return 1
    if n == 3:
        return 3
    maximum
    minOne = 1
    minTwo = 1
    for i in range(2,n+1):
        maximum = 2*minOne + minTwo
        minOne = maximum
    return max
'''
        EVERYTHING ABOVE THIS IS FOR THE PREVIOUS QUESTIONS
Problem 2 not considering space usage
    notes: consider max(array[i-1],array[i-2] + i)  , store these in variables
'''
def maxGrade(array):
    size = len(array)
    if size == 0:
        return array[0]
    if size == 1:
        return max(array[0],array[1])

    memo = []
    memo.append(array[0])
    memo.append(array[1])
    for i in range(2,size):
        memo.append(max(memo[i-1], memo[i-2] + array[i]))
    return memo[i]

'''
Problem 2 with efficent space usage
    notes: consider max(array[i-1],array[i-2] + i)  , store these in variables
    we make this function take O(1) space by only holding the previous maximum value or the new maximum value considering the current iterations value
'''
def maxGrade_Efficient(array):
    size = len(array)
    if(size == 0):
        return array[0]           # if there is only one item it must be the max elee
    if(size == 1):
        return max(array[0], array[1])         # if there are two items just take the max of either of them
    currentMax = array[1]
    maxConsideringIndex = array[0]
    for i in range(2,size):
        if((maxConsideringIndex+array[i]) < currentMax):  # dont take the new item
            maxConsideringIndex = currentMax
            print("CurrentMax: ", maxConsideringIndex)
        else:                                             # take the item, but the new max needs to be calculated
            temp = currentMax
            currentMax = maxConsideringIndex + array[i]
            maxConsideringIndex = temp
            print("CurrentMax: ", currentMax)
    if (maxConsideringIndex > currentMax):          # we have found a solution that is better
        return maxConsideringIndex
    else:
        return currentMax                           # didn't find a solution that is bette r

def main():
    # ALL OF THIS IS FOR THE FIRST TWO QUESTIONS
    n = 5
    array = [None]*2**n   # array for memoization

    print("UNMEMOIZED VERSION")
    start = timeit.timeit()         #normal version
    result = pellNum(n)
    print("RESULT:", result)
    end = timeit.timeit()
    print(start - end)

    print("--------")
    print("MEMOIZED VERSION")

    start = timeit.timeit()             # memoized version , this one is awesome runtime
    result_memo = pellNum_memo(array,n)
    print("MEMO RESULT:", result_memo)
    end = timeit.timeit()
    print(start - end)

    print("=============================")

    # THIS PART OF THE MAIN IS FOR PROBLEM 2
    array = [2,7,9,3,1]

    print("Running Inefficient MaxGrade")
    print("Maximum", maxGrade(array))
    print("--------")
    print("Running Effecient MaxGrade")
    print("Maximum", maxGrade_Efficient(array))

if __name__ == '__main__':
    main()
items = ['snickers','chicken','steak']
proteinArray = ['399','400','500']
caloriesArray = ['90','75','150']
MAXCALORIE = 150
def maxProtein(proteinArray,caloriesArray,MAXCALORIE):
    if len(proteinArray) == 1:  # base case
        return MAXCALORIE%caloriesArray[0] * proteinArray[0]        # determines how many cups you can fit into caloric limit
                                                                    # then gets you the total amount of protein you just maximized
    if len(proteinArray) == 2:
        return max(MAXCALORIE%caloriesArray[0] * proteinArray[0],MAXCALORIE%caloriesArray[1] * proteinArray[1])
    memo = []




'''
# this works fine, but for assignment i dont think we are allowed to memoize via dictionary
pell_memo = {}
def pellNum_memo_dictionary(n):
    if n == 1 or n == 0:
        return 1
    if n not in pell_memo:
        pell_memo[n] = 2*pellNum_memo(n-1) + pellNum_memo(n-2)
    return pell_memo[n]
'''
