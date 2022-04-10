
arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

def threeNumberSum(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr)):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            currentSum = arr[i] + arr[l] + arr[r]
            if currentSum == target:
                result.append([arr[i], arr[l], arr[r]])
                l+=1
                r-=1
            elif currentSum < target:
                l+=1
            else:
                r-=1
    return result


print(threeNumberSum(arr, target))
