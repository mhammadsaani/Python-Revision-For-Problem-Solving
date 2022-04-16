arr = [1, 2, 3, 3, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 6, 5, -1, -2, -3, 2, 3]

def longestPeak(arr):
    peak = 0
    currentPointer = 1
    while currentPointer != len(arr) - 1:
        if arr[currentPointer - 1] < arr[currentPointer] and arr[currentPointer] > arr[currentPointer+1]:
            tempPeak = 3
            pointer = currentPointer + 1
            while arr[pointer] > arr[pointer+1]:
                pointer += 1
                tempPeak += 1

            if tempPeak > peak:
                peak = tempPeak
        currentPointer += 1

    return peak

print(longestPeak(arr))