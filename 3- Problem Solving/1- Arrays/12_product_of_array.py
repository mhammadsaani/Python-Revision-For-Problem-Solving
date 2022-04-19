

# with Division

arr = [5, 1, 4, 2]

def productOFArray(arr):
    product = 1
    resultArr = [0 for _ in arr]
    for i in arr:
        product *= i

    for i in range(len(resultArr)):
        resultArr[i] = product / arr[i]
    

    return resultArr



# If division not allowed || Product Of Array || Time O(N) | Space O(N)

arr = [5, 1, 4, 2]

def productOfArray2(arr):
    leftCurrentElement = 1
    rightCurrentElement = 1
    leftArray = [1 for _ in range(len(arr))]
    rightArray = [1 for _ in range(len(arr))]

    for i in range(len(arr)):
        leftArray[i] = leftCurrentElement
        leftCurrentElement *= arr[i]

    for i in range(len(arr)-1, -1, -1):
        rightArray[i] = rightCurrentElement
        rightCurrentElement *= arr[i]

    for i in range(len(arr)):
        arr[i] = leftArray[i] * rightArray[i]

    print(leftArray, rightArray, arr)

productOfArray2(arr)