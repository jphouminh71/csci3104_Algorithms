import numpy

'''                     Was going to use this check how similar two strings are
# compare this number to what the maxium count is for the target string
def count_operations(operation_array, insertCost, subCost, deleteCost):
    count = 0
    for i in range(len(operation_array)):
        if operation_array[i] != "*":
            if operation_array[i] == "Insert":
                count = count + insertCost
            elif operation_array[i] == "Delete":
                count = count + deleteCost
            elif operation_array[i] == "Subsutition":
                count = count + subCost
    return count
'''

'''
    This function is just used to read in the input from the two text files,
    it also strips all whitespaces
'''
def getInputString(filename1,filename2):
    instream = open(filename1, "r")
    instream2= open(filename2, "r")
    string1 = ""
    string2 = ""
    for line in instream:
        string1 = string1 + line.replace(" ","")
    for line in instream2:
        string2 = string2 + line.replace(" ","")
    return string1,string2
'''
    this is just a helper function that prints the contents of the vector of common
    substrings
'''
def printCommonSubstrings(arr):
    print("======================")
    print("PRINTING COMMON SUBSTRINGS OF AT LEAST SIZE L")
    print("======================")
    for i in range(len(arr)):
        print(arr[i])
    print("----------------------")
'''
    this is another helper function that prints out the cost table of the strings
'''
def printTable(matrix,source,target):
    for i in range(len(source)):
        print(' ',source[i], end='\0')
    print(' ')
    for i in range(len(target)):
        print(' ',target[i], end='\0')
    print()
    for row in matrix:
        print(row)

'''
    going to assume that this function isn't called with empty values,
    this array fills in a array with substrings that are at least of length L.
    We decide what counts as a substring by saving characters that are between
    operations that are not no ops (*), once two no ops are found
    the substring will be saved in the vector.

----------------------------------------------------------------------------------------
    RUNTIME ANALYSIS OF commonSubstrings
----------------------------------------------------------------------------------------
    This function traverses a single array only once so the runtime of this function is
    O(n).
'''
def commonSubstrings(string_x, integer_L, operations):
    sub_str_arr = []
    i = 0
    size = len(string_x)
    current_subsqnc = ""
    while i < size:
        if (operations[i] != "*"):
            if (current_subsqnc != "" and len(current_subsqnc) >= integer_L):
                sub_str_arr.append(current_subsqnc)
            current_subsqnc = ""
            i = i + 1
        else:
            current_subsqnc = current_subsqnc + string_x[i]
            i = i + 1
    return sub_str_arr
'''
    Extract Alignment function takes in the costTable,source,target, and costs of inserts
    we find the alignment table by backtracing from the bottom right indice of the cost
    matrix. We decide which operation was made to get to that subproblem by finding
    the minimum operation cost of the cells diagnolly left from the current cell, the top
    and the left cell of the array. After we find the minimum of the surrounding cells
    we append the operation name into the operation array and then recursively move to the next
    cell to be processed.

----------------------------------------------------------------------------------------
    RUNTIME ANALYSIS OF extractAlignment
----------------------------------------------------------------------------------------
    Our recurrence is T(n) = T(n-1) + 1 therefore our runtime of our function is in
    O(n)
'''
def extractAlignment(costTable,source,target,insertCost, deleteCost, subCost,i,j,A):
    if(i == 0 or j == 0):
        return
    minimum = min(costTable[i][j-1],costTable[i-1][j-1],costTable[i-1][j])
    if (minimum == costTable[i-1][j-1] and costTable[i-1][j-1] == costTable[i][j]):
        j = j - 1
        i = i - 1
        A.append("*")       # stop denotes no op
    elif (minimum == costTable[i][j-1]):
        j = j-1
        A.append("Insert")
    elif (minimum == costTable[i-1][j]):
        i = i -1
        A.append("Delete")
    else:
        i = i-1
        j = j-1
        A.append("Subsutition")
    return (extractAlignment(costTable,source,target,insertCost,deleteCost,subCost,i,j,A))


'''
    Function align strings takes a source input target input and the cost of all the operations, then the function
    will return list of operations that are required to transform the source string into the target string. I went
    about solving this problem by first attempting to construct a 2d matrix of the size of source * target. I kept
    running into indexing errors so i attempted to force this function to not have indexing errors by making the source
    and target string lengths equal to eachother but i do realize that this does bump up the run time from O(n * m)
    to O(n^2). Following this change i went about filling the matrix by following the steps to fill out the matrix by hand
    which is first filling the first row and first column with values 0. . . n. Then filling out cells by
    finidng the minimum surrounding cell values.

----------------------------------------------------------------------------------------
    RUNTIME ANALYSIS OF alignStrings
----------------------------------------------------------------------------------------
    The true runtime of this function should just be in O(n * m) complexity but since
    we implemented in a way such that we made both strings the same length to try and avoid
    indexing errors we actually end up getting a worse runtime of O(n^2).
'''
# this function is just supposed to return the who
def alignStrings(source,target,insertCost,deleteCost,subCost):
    source = "_" + source
    target = "_" + target
    size_source = len(source)
    size_target = len(target)

    # edge case if strings are empty
    if (size_source == 1) or (size_target == 1):
        return 0
    # match the string sizes
    if len(source) < len(target):
        source = source + target[len(source)]
    if len(target) < len(source):
        target = target + source[len(target)]
    size_source = len(source)
    size_target = len(target)

    # build the matrix that is dependent on the strings sizes
    costMatrix = [[0 for i in range(size_source)] for i in range(size_target)]

    # now we start building the actual table, start with the trivial answers for "_" character
    for i in range(size_source):
        costMatrix[0][i] = i * insertCost
        costMatrix[i][0] = i * deleteCost

    # now start filling the non-trivial solutions, index j = 1 i = 1
    for i in range(1,size_source):
        for j in range(1,size_target):
            # first edge case check against a hard match, this will be a no-op
            if source[i] == target[j]:
                #print("HARD MATCH: ",source[i],target[j])
                costMatrix[i][j] = costMatrix[i-1][j-1]  # this is the value that is directly diagnol from the cell
            # if its not this, we just check the minimum cost of its surrounding cells
            else:
                #print("FINDING MIN!")
                minimum = min(
                    costMatrix[i-1][j-1]+subCost,     # substitution
                    costMatrix[i-1][j]+insertCost,       # dle
                    costMatrix[i][j-1]+deleteCost        # insertion
                )
                if (costMatrix[i-1][j-1]+1):
                    #print("Performed an substitution")
                    costMatrix[i][j] = minimum
                elif (costMatrix[i-1][j]+1):
                    #print("Performed a insertion")
                    costMatrix[i][j] = minimum
                else:
                    #print("Performed a Deletion")
                    costMatrix[i][j] = minimum
    return costMatrix,source,target
def main():
    # this is only used for printing since in align string we manipulated the strings
    o_source = "POLYNOMIAL"
    o_target = "EXPONENTIAL"

    # these are used for the functions
    source = "POLYNOMIAL"
    target = "EXPONENTIAL"

    insertCost = 2
    deleteCost = 1
    subCost = 2
    L = 2
    ops = []
    sub_str_arr = []

    input1 = "Song1_Folsom_Prison.txt"
    input2 = "Song2_Crescent_City_Blues.txt"


    # alignStrings returns the cost table matrix , use this table in extraction
    costTable,source,target = alignStrings(source,target,insertCost,deleteCost,subCost)
    print("======================")
    print("PRINTING OUT COST TABLE FOR, SOURCE = ", o_source," AND TARGET = ", o_target)
    print("======================")
    printTable(costTable,source,target)
    i = len(source)-1
    j = len(target)-1

    extractAlignment(costTable,source,target,insertCost,deleteCost,subCost,i,j,ops)
    sub_str_arr = commonSubstrings(source, L, ops)
    printCommonSubstrings(sub_str_arr)


    print("EVERYTHING IS FOR PLAGERISM CHECK")
    insertCost_2 = 1
    deleteCost_2 = 1
    subCost_2 = 1
    student_ops = []
    studentString = ""
    realSong = ""
    studentString, realSong=getInputString(input1,input2)
    student_ops=alignStrings(studentString,realSong,insertCost_2,deleteCost_2,subCost_2)

    '''
        Attemping to put the string of input into our functions we get a segmentation error
    so I will explain the logic behind this problem. We first take in the two input files text into
    string variables and strip all whitespaces in each to make the runtime a bit faster and then we
    should have passed it into the alignStrings and extractAlignment functions. Once we have the operation
    array for the string containing the students song we can look out how many matching sequences there are
    compared to the the real song. We determine if the students song is a case of plagerism if by comparing the
    ratio of matches in the students song to the real song and seeing if there is at least a 40% ( this value is
    ambigous to my choice).
    '''





main()
if __name__ == '_main_':
    main()
