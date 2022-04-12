from shutil import move


arr = [1, 2, 2, 2, 3,  4, 2]
target = 2

def swap(arr, idxTarget, lastIdx):
    temp = arr[idxTarget]
    arr[idxTarget] = arr[lastIdx]
    arr[lastIdx] = temp


def moveElementToEnd(arr, target):
    occurence = 0
    for i in arr:
        if i == target:
            occurence += 1
    lastIdx = len(arr) - 1
    for i in range(len(arr)):
        while arr[i] == target:
            swap(arr, i, lastIdx)
            lastIdx -= 1
            occurence -= 1
            if occurence == 0:
                break

        if occurence == 0:
            break
    print(arr)


def moveElementToEnd(arr, target):
    currentLastIdx = len(arr) - 1
    for i in range(len(arr)):
        while arr[i] == target and arr[currentLastIdx] != target:
            swap(arr, i, currentLastIdx)
            currentLastIdx -= 1


print(moveElementToEnd(arr, target))