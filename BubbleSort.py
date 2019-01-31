import random
##Bluesort
#Signed~AdamShea
totalNumbersInPlay = 1000+1
listOfNums = []
i = 0

while i != totalNumbersInPlay:
    listOfNums.append(random.randint(0,10000))
    i+=1

listLen = len(listOfNums)   ##Length of list of nums
maxi = 0
i=0
while i < listLen and i != totalNumbersInPlay-1:
    if listOfNums[i] < listOfNums[i+1]:
        temp1 = listOfNums[i]   #Stores current numbers
        temp2 = listOfNums[i+1]
            
        listOfNums[i] = temp2   ##Swaps over numbers
        listOfNums[i+1] = temp1
        if i > maxi+10:
            maxi = i
            print("Current iteration :"+str(maxi))
        i=0
    else:
        i+=1

print(listOfNums)
