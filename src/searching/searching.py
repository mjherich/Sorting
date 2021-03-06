# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  # Check first and last element in array before main loop
  if arr[0] == target:
    return 0
  elif target < arr[0]:
    return -1
  if arr[-1] == target:
    return len(arr)-1
  elif target > arr[-1]:
    return -1

  while low < high - 1:
    mid = (high+low) // 2
    if arr[mid] == target:
      return mid
      break
    elif target < arr[mid]:
      high = mid
    elif target > arr[mid]:
      low = mid
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle-1)
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle+1, high)
  else:
    return middle