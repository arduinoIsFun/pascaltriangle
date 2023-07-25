import sys
def pascalCreate(n,nRow = []):
    tempList = [] #Create an empty list
    if n == 0: #Default case when there are zero rows
        return [str(1)]
    #If not default go to recursive case
    else:
        if n == 1: #Row 1 default case
            for i in range(2):
                tempList.append(str(0 + int(pascalCreate(n-1,nRow)[0])))
        else:
            previousRow = pascalCreate(n-1) #Get the previous row since all pascal triangle rows are based on each other
            for i in range(n+1): #Repeat for all elements in the nth pascal triangle row
                if i == 0 or i == len(previousRow):
                    tempList.append(str(0+int(previousRow[0])))
                else:
                    tempList.append(str(int(previousRow[i]) + int(previousRow[i-1])))
        nRow = tempList
        return nRow

def getGreatestLength(n):
    pascalList = pascalCreate(n)
    myString = ''.join(pascalList)
    length = len(myString) + len(pascalList) + 1
    return length

n = int(input("Enter the number of rows wanted for Pascal's Triangle: "))
if n <= 0:
    sys.exit("Input must be a positive integer")

#Part of the formating when writing to a file
else:
    prefix = getGreatestLength(n-1)
    outFile = open("Pascal_Triangle_of_" + str(n) + "_rows.txt","w")
    for i in range(n):
        myList = pascalCreate(i)
        myString = ' '*round((abs(prefix-len(''.join(myList))-len(myList)+1))/2)
        for k in range(len(myList)):
            if k == len(myList) - 1:
                myString += str(myList[k])
            else:
                myString += str(myList[k]) + ' '
        if i != n-1:
            outFile.write(myString + '\n')
        else:
            outFile.write(myString)
    outFile.close()
