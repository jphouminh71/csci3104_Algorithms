


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





def main():
    input1 = "Song1_Folsom_Prison.txt"
    input2 = "Song2_Crescent_City_Blues.txt"

    readInput(input1,input2)


if __name__ == '__main__':
    main()
