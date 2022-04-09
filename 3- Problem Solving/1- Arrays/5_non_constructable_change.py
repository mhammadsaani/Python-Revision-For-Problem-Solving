

array = [5, 7, 1, 1, 2, 3, 22]

# Time O(N Log N) | O (1)
def nonConstrutibleChange(array):
  array.sort()
  print(array)
  change = 0
  for i in array:
    if change < i:
      return change + 1
    change += i
    
print(nonConstrutibleChange(array))