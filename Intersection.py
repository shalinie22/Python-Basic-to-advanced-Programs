# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

def FindIntersection(strArr):

  # code goes here
  arr1 = [int(i) for i in strArr[0].split(",")] 
  arr2 = [int(i) for i in strArr[1].split(",")]
  newlist = sorted(list(set(arr1) & set(arr2))) 
  return newlist if newlist else "false"

# keep this function call here 
print(FindIntersection(input()))