def ArrayChallenge(arr):
  arrToken = "r4vc9ywieb1"
  ans = []
  
  if len(arr) > 3:
    ans =  [arr[1], arr[-2]]
  else:
    ans =  [arr[0], arr[-1]]

  temp = str(ans[0]) + "X" + str(ans[1])
  tempLen = len(temp)
  arrToken = temp + arrToken
  tempStr = ""
  for i in range(tempLen + 1, len(arrToken), 2):
    tempStr = arrToken.replace(str(arrToken[i]), "X", 1)
    
  return tempStr


# keep this function call here 
print(ArrayChallenge(input()))