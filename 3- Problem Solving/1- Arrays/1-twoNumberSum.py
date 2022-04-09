sampleInput = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
dic = {}

# O(n) time | O(n) space || Method_1


def twoNumberSum(array, target):
  for num in sampleInput:
    if target - num in dic:
      return [target - num, num]
    else:
      dic[num] = True
  return []

a=sampleInput.index(5)
print(a)

# Method_1 using enumerate

def twoSum(nums, target):
  values = {}
  for idx, value in enumerate(nums):
    if target - value in values:
        return [values[target - value], idx]
    else:
        values[value] = idx



sampleInput = [3, 5, -4, 8, 11, 1, -1, 6]
target = 6


def twoSum(nums, target):
  dic = {}
  for i in range(len(nums)):
    if target - nums[i] in dic:
      return [nums.index(target - nums[i]), i]
    else:
      dic[nums[i]] = True

  return []


print(twoSum(sampleInput, target))


# Time O(n log n) || Method_2

sampleInput = [3, 5, -4, 8, 11, 1, -1, 6]
target = 14


def twoSumLR(sampleInput, target):
  nums = sampleInput
  left = 0
  right = 0
  nums.sort()
  while left < right:
    currentSum = nums[left] + nums[right]
    if currentSum == target:
      return [left, right]
    elif currentSum < target:
      left+=1
    else:
      right-=1           
  return []

print(twoSumLR(sampleInput, target))