
# Approach One

def isMonotonic(nums):
    if nums[0] < nums[-1]:
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                continue
            return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]:
                continue
            return False
    return True


# Approach One Optimized 

def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            isIncreasing = False
        if nums[i] > nums[i+1]:
            isDecreasing = False
    
    return isDecreasing or isDecreasing