def isValidSubsequence(array, sequence):
	
  c = 0
  for i in range(len(array)):
    x = sequence[c]
    if c == len(sequence):
        break
    if array[i] == x:
      c+=1
  return c == len(sequence)



array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]


print(isValidSubsequence(array, sequence))