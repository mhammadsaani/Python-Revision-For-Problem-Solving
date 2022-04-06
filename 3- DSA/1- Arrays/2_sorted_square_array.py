# You have to return a sorted square array , you would be given a sorted array

# [1, 2, 3, 4, 5, 6] outputs [1, 4, 9, 16, 25, 36]

# Approach 1 | Time O(N)

numsPositive = [1, 2, 3, 4, 5, 6]
numMixNumbers = [-2, -1, 4, 7, 9]
def sortedSquareArray(nums):
  for index, num in enumerate(nums):
    nums[index] = num * num
  return nums

print(sortedSquareArray(numsPositive))
print(sortedSquareArray(numMixNumbers))

# but this approach will not work if array has negative numbers :-(

# Approach 2 | Time O(n log n) 

numsPositive = [1, 2, 3, 4, 5, 6]
numMixNumbers = [-2, -1, 4, 7, 9]

def sortedSquareArray(nums):
  for index, num in enumerate(nums):
    nums[index] = num * num
  nums.sort()
  return nums

print(sortedSquareArray(numsPositive))
print(sortedSquareArray(numMixNumbers))


# Optimized Approach | Time O(N) , Space O(N)

# - we use l < = r because for the last element l == r. abs(num) returns the absolute value.

numsPositive = [1, 2, 3, 4, 5, 6]
numMixNumbers = [-2, -1, 4, 7, 9]


def square(num):
  return num * num

def sortedSquareArray(nums):
  l = 0
  r = len(nums) - 1
  array = [0 for _ in nums]
  le = len(array) - 1
  while (l <= r):
    leftSquare = square(abs(nums[l]))
    rightSquare = square(abs(nums[r])) 
    if leftSquare > rightSquare:
      l+=1
      array[le] = leftSquare
      le -= 1
    else:
      r-=1
      array[le] = rightSquare
      le -= 1
  return array

print(sortedSquareArray(numsPositive))
print(sortedSquareArray(numMixNumbers))


# test = [1, 2, 3, 4, 5]
# test2 = [0 for _ in test]
# print(test2)