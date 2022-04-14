arr = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]


def spiralTraverse(arr):
    result = []
    sC = 0
    eC = len(arr[0]) - 1
    sR = 0
    eR = len(arr) - 1

    while sC <= eC and sR <= eC:
        for row in range(sC, eC+1):
            result.append(arr[sR][row])

        for col in range(sR+1, eR+1):
            result.append(arr[col][eR])

        for revRow in range(eC-1, sC-1, -1):
            result.append(arr[eR][revRow])

        for revCol in range(eR - 1, sR, -1):
            result.append(arr[revCol][sC])

        sR += 1
        eR -= 1
        sC +=1 
        eC -= 1

    return result



def spiralTraverse(arr, result, sR, eR, sC, eC):

    if sC > eC and sR > eC:
        return result

    for row in range(sC, eC+1):
        result.append(arr[sR][row])

    for col in range(sR+1, eR+1):
        result.append(arr[col][eR])

    for revRow in range(eC-1, sC-1, -1):
        result.append(arr[eR][revRow])

    for revCol in range(eR - 1, sR, -1):
        result.append(arr[revCol][sC])


    return spiralTraverse(arr, result, sR+1, eR-1, sC+1, eC-1)



print(spiralTraverse(arr, [], 0, len(arr) - 1, 0 , len(arr) - 1))