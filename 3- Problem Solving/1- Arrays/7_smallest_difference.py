lTwo = [-1, 5, 10, 20, 28, 3]
lOne = [26, 134, 135, 15, 17]


# Method 1 | Time O(N*2) 

def smallestDifference(arrOne, arrTwo):
    arrOne.sort()
    arrTwo.sort()
    check = 100
    result = []
    if len(arrOne) < len(arrTwo):
        temp = arrOne
        arrOne = arrTwo
        arrTwo = temp
    for i in range(len(arrOne)):
        for j in range(len(arrTwo)):
            if arrOne[i] - arrTwo[j] < check and arrOne[i] - arrTwo[j] >= 0:
                result = [arrOne[i], arrTwo[j]]

    return result


lTwo = [-1, 5, 10, 20, 28, 3]
lOne = [26, 134, 135, 15, 17]

# Method 2 | O(nlogn + mlogm) where n = len(arrOne) and m = len(arrTwo)

def smallestDifference(arrOne, arrTwo):
    arrOne.sort()
    arrTwo.sort()
    ll = 0
    rl = 0
    while (ll != len(arrOne) - 1 and rl != len(arrTwo) - 1):
        currentDiff = arrOne[ll] - arrTwo[rl]
        if currentDiff == 0:
            return [arrOne[ll], arrTwo[rl]]
        if arrOne[ll] < arrTwo[rl]:
            currentDiff = arrTwo[rl] - arrOne[ll]
            ll += 1
        else:
            rl += 1

    return [arrOne[ll], arrTwo[rl]] 



print(smallestDifference(lOne, lTwo))