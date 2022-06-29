import sys

arr = [2, 4, 1, 2, 4, 4, 5]

# O(N*2)

def firstOccurenceDuplicate(arr):
    minimunIndex = len(arr)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if j < minimunIndex:
                    minimunIndex = j

    return minimunIndex




def firstOccurenceDuplicate2(arr):
    dic = {}
    c = 0
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[c] = arr[i]
            c+=1
        else:
            return i + 1

def firstOccurenceDuplicate2I(arr):
    s = set()
    for i in arr:
        if i in s:
            return i
        s.add(i)

    return -1
        


arr = [5, 1, 3, 2, 1, 5]

def firstOccurenceDuplicate3(arr):
    for i in range(len(arr)):
        idx = arr[i] - 1
        arr[i] = arr[idx]
        if arr[i] == -1:
            return i
        arr[idx] = -1
    return -1   



print(firstOccurenceDuplicate3(arr))




