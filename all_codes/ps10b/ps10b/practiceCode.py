import numpy



def printTable(matrix,source,target):
    if (source == "") or (target == ""):
        print("EMPTY MATRIX")
        return 0
    for i in range(len(source)):
        print(' ',source[i], end='\0')
    print(' ')
    for i in range(len(target)):
        print(' ',target[i], end='\0')
    print()
    for row in matrix:
        print(row)

# this function is just supposed to return the who
def alignStrings(source,target,insertCost,deleteCost,subCost):
    if (source == "") or (target == ""):
        return 0,"",""
    if len(source) ==  len(target):
        source = "_" + source
        target = "_" + target
    elif len(source) > len(target):     # match the rest of the target string 
        continue
    elif len(target) > len(source):

    size_source = len(source)
    size_target = len(target)

    # edge case if strings are empty


    # build the matrix that is dependent on the strings sizes
    costMatrix = [[1 for i in range(size_source)] for i in range(size_target)]

    printTable(costMatrix,source,target)
    # now we start building the actual table, start with the trivial answers for "_" character

    for i in range(size_target):
        costMatrix[0][i] = i * insertCost
        costMatrix[i][0] = i * deleteCost


    # now start filling the non-trivial solutions, index j = 1 i = 1
    for i in range(1,size_source):
        for j in range(1,size_target):
            # first edge case check against a hard match, this will be a no-op
            if source[i] == target[j]:
                print("HARD MATCH: ",source[i],target[j])
                costMatrix[i][j] = costMatrix[i-1][j-1]  # this is the value that is directly diagnol from the cell
            # if its not this, we just check the minimum cost of its surrounding cells
            else:
                print("FINDING MIN!")
                minimum = min(
                    costMatrix[i-1][j-1]+subCost,     # substitution
                    costMatrix[i-1][j]+insertCost,       # insertion
                    costMatrix[i][j-1]+deleteCost        # deletion
                )
                if (costMatrix[i-1][j-1]+1):
                    print("Performed an substitution")
                    costMatrix[i][j] = minimum
                elif (costMatrix[i-1][j]+1):
                    print("Performed a insertion")
                    costMatrix[i][j] = minimum
                else:
                    print("Performed a Deletion")
                    costMatrix[i][j] = minimum

    return costMatrix,source,target
def main():
    source = "pla"
    target = "plane"

    insertCost = 2
    deleteCost = 2
    subCost = 2

    # alignStrings returns the cost table matrix , use this table in extraction
    costTable,source,target = alignStrings(source,target,insertCost,deleteCost,subCost)
    printTable(costTable,source,target)

main()
if __name__ == '_main_':
    main()
