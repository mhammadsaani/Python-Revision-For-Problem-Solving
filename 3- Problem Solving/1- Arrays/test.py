import sys
# def ArrayChallenge(arr):
#   arrToken = "r4vc9ywieb1"
#   ans = []
  
#   if len(arr) > 3:
#     ans =  [arr[1], arr[-2]]
#   else:
#     ans =  [arr[0], arr[-1]]

#   temp = str(ans[0]) + "X" + str(ans[1])
#   tempLen = len(temp)
#   arrToken = temp + arrToken
#   tempStr = ""
#   for i in range(tempLen + 1, len(arrToken), 2):
#     tempStr = arrToken.replace(str(arrToken[i]), "X", 1)
    
#   return tempStr


# # keep this function call here 
# print(ArrayChallenge(input()))



# Two Number SUm 

# sampleInput = [3, 5, -4, 8, 11, 1, -1, 6]
# target = 10

# def twoNumberSum(array, target):
#   for i in range(len(sampleInput)):
#     for j in range(len(sampleInput)):
#       if i + j == target:
#         return [i, j]
  


# def twoNumberSum2(array, target):
#   array.sort()
#   l = 0
#   r = len(array) - 1
#   print(array)
#   while l <  r:
#     currentNum = array[l] + array[r]
#     if currentNum == target:
#       return [array[l], array[r]] 
#     elif currentNum < target:
#       l+=1
#     else:
#       r+=1

#   return []
    


# def twoNumberSum3(arr, target):
#   dic = {}
#   for i in range(len(arr)):
#     if target - arr[i] in dic:
#       return [i, dic[target - arr[i]]]
#     else:
#       dic[arr[i]] = i

#   return []

# # --------------

# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [22, 6, 25]

# def isValidSubsequence(array, sequence):
#   j = 0
#   for i in range(len(array)):
#     if sequence[j] == array[i]:
#       j+=1
#     if j == len(sequence):
#       return True

#   return False


# # print(isValidSubsequence(array, sequence))


# numsPositive = [1, 2, 3, 4, 5, 6]
# numMixNumbers = [-2, -1, 4, 7, 9]


# def square(num):
#   return num * num



# def sortedSquareArray(array):
#   result = [0 for _ in array]
#   l = 0
#   r = len(array) - 1
#   pointer = len(result) - 1
#   while l <= r:
#     leftSquare = square(abs(array[l]))
#     rightSquare = square(abs(array[r]))
#     if leftSquare < rightSquare:
#       result[pointer] = rightSquare
#       pointer-=1
#       r-=1
#     else:
#       result[pointer] = leftSquare 
#       pointer-=1
#       l+=1
#   return result



# competition = [['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']]
# results = [0, 0, 1]


# def tournmentWinner(arr, result):
#   currentWinner = ""
#   finalWinner = ""
#   dic = {finalWinner: 0}
#   for i in range(len(competition)):
#     if result[i] == 0:
#       currentWinner = competition[i][1]
#     else:
#       currentWinner = competition[i][0]
#     if currentWinner not in dic:
#       dic[currentWinner] = 1
#     else:
#       dic[currentWinner] += 1
#     if dic[finalWinner] < dic[currentWinner]:
#       finalWinner = currentWinner
#       dic[finalWinner] = dic[currentWinner]

#   return [finalWinner, dic[finalWinner]]
    
# print(tournmentWinner(competition, results))


# arr = [1, 2, 3, 4]

# def minAbsoulteDiff(arr):
#   arr.sort()
#   minAbsoluteDiff = arr[1] - arr[0]
#   result = []
        
#   for i in range(len(arr) - 1, 1, -1):
#     if arr[i] - arr[i-1] == minAbsoluteDiff:
#         result.append([arr[i-1], arr[i]])
                
#   return result

# print(minAbsoulteDiff(arr))



# dic = {1: [1, 2, 3], 2: [2, 3, 4]}


# def factorial(n):
#     if n < 2:
#         return n
    
#     return n * factorial(n-1)


# print(factorial(6))

print(sys.argv[0])