# Finding max element in an array without using sort
# Assume an array arr
maxEle = arr[0]
for i in arr:
    if i > maxEle:
       maxEle = i
return maxEle

# Second Largest element in an array
largest = arr[0]
Slargest = 0
for i in arr:
    if i > largest:
        Slargest = largest
        largest = i
    
return Slargest

# Find if the array is sorted without using sort method
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        return False
        break    
else:
    return True

# Remove duplicates from sorted array
i = 0
for j in range(len(arr)):
    if arr[i] != arr[j]:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    
return i + 1
