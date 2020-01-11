import numpy
'''
   This function should take no longer than O(nt), this cost is coming from creating the truth table in the function ksum
   where we need to go through every possible scenario to determine the final result.
   Also the runtime of the backtracing function should take no longer than O(n) since it is always going at least one step back closer
   to hitting the base case for when row or col is less than or equal to zero.
   
   Therefore, this program will run in O(nt) 
    
'''
'''
    function will return true or false depeending on if k set of numbers add up to target
'''
def backtrace(matrix,subset,row,col,subset_size,target):   # the runtime of this function should take no longer than O(n)
    col = col
    row = row
    subset_uptoK = []
    if matrix[row][col] == 1:
        while ( row > 0 and col > 0):
            if subset[row-1] < target:
                print("TAKING LAST ELEMENT: ", subset[row-1])
                subset_uptoK.append(subset[row-1])
                #subset[row-1] = target+1
                col = col-subset[row-1]
                row = row - 1
            elif (matrix[row-1][col] == 1 and subset[row-1] > target):
                #cell = matrix[row-1][col]
                row = row -1
            elif (matrix[row-1][col] == 0 and subset[row-1] > target):
                print("TAKING:", subset[row-1])
                matrix[row][col] = -1   # mark in the table which one you just took, it makes it easier to see
                subset_uptoK.append(subset[row-1])
                #cell = matrix[row-1][col-subset[row-1]]
                col = col-subset[row-1]
                row = row -1
                print(matrix)
        return subset_uptoK
    else:
        return False
'''
    function creates a dp table 1's are TRUE and 0's

    RUNTIME: Runtime of this function should take no longer than (n*m) where n is the array size and m is all the values of k from 1 .. k
'''
def ksum(subset,subset_size,target):
    table = numpy.arange(((len(subset))+1)*(target+1)).reshape(((len(subset))+1, target+1)) #Table made and we will change the values when need.
    for row in range(len(subset)+1):    # loop through every item in the subset including a 0 subset
        for col in range(target+1):  # loop through every vale for target - 1
            if row == 0 and col != 0:  # the other trivial solution
                table[row][col] = 0
            elif col == 0:        # trivial solution to when current k value is equal to 0, anything could be summed up to 0
                table[row][col] = 1
            elif (row >= 0):
                if (subset[row-1] == col):  #looking at the actual array, if the numbers match then its a true
                    table[row][col] = 1
                elif(table[row-1][col] == 1):  # look at if the cell above it is true, if it is then we know its true too
                    table[row][col] = 1
                # otherwise we will look back to previous answers in our solution to figure out if the current cell is true or false
                elif (table[row-1][col-subset[row-1]] == 1 and col > subset[row-1]):
                    table[row][col] = 1
                else:
                    table[row][col] = 0
    return table,row,col
def main():
    '''
    Input:  s ={2,1,5,7}, t = 4, k = 2
    Output:  FalseExplanation:  No subset of size 2 sums to 4.
    Input:  s ={2,1,5,7}, t = 6, k = 2
    Output:{1, 5}
    Explanation:  Subset{1, 5}has size 2 and sums up to the targett= 6.
    Input:  s ={2,1,5,7}, t = 6, k = 3
    Output:  False
    Explanation:  No subset of size 3 sums to 6.
    '''
    #test1 = [1,3,2]
    test2 = [2,1,5,7]

    subset_size = 2
    target = 4
    matrix,row,col = ksum(test2,subset_size,target)
    print("ARR:",test2," TARGET: ",target," KSIZE:",subset_size)
    print(matrix)
    subset_found = backtrace(matrix,test2,row,col,subset_size,target)

    if subset_found == False:
        print("NO SOLUTION")
        return False
    else:
        print(subset_found)
        if len(subset_found) == subset_size:
            print("CORRECT")
            return True
        else:
            print("NOT CORRECT")
            return False

if __name__ == '__main__':
    main()
