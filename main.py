
#---------------------------------------------------------------
def findFirstMin(arr):
    firstMin = arr[0]
    for i in range(1,len(arr)):
        firstMin = min(firstMin, arr[i])
    return firstMin
#---------------------------------------------------------------
def findSecondMin(arr):
    if len(arr) < 2:
        return "error"

    firstMin = min(arr[0], arr[1])
    secondMin = max(arr[0], arr[1])
    for i in range(1,len(arr)):
        if arr[i] < secondMin:
            if arr[i] < firstMin:
                secondMin = firstMin
                firstMin = arr[i]
            else:
                secondMin = arr[i]

    return secondMin
#---------------------------------------------------------------
def findmthMin(arr, m):
    if len(arr) < m:
        return "error"

    pivot = arr[0]
    left = []
    right = []
    for item in arr[1:len(arr)]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    pivotIndex = len(left)
    if pivotIndex+1 is m:
        return pivot
    elif pivotIndex+1 > m:
        return helper(left, m, pivotIndex-len(left)-1)
    elif pivotIndex+1 < m:
        return helper(right, m, pivotIndex+1)

def helper(arr, m, pivotIndex):
    if len(arr) <= 1:
        if pivotIndex+1 == m:
            return arr[0]

    pivot = arr[0]
    left = []
    right = []
    for item in arr[1:len(arr)]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    pivotIndex = pivotIndex + len(left)
    if pivotIndex+1 == m:
        return pivot
    elif pivotIndex+1 > m:
        return helper(left, m, pivotIndex-len(left))
    elif pivotIndex+1 < m:
        return helper(right, m, pivotIndex+1)

#---------------------------------------------------------------
def findmthMin2(arr, m):
    if len(arr) < m:
        return "error"

    pivot = arr[0]
    left = []
    right = []
    for item in arr[1:len(arr)]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    pivotIndex = len(left)
    if pivotIndex+1 is m:
        return pivot
    elif pivotIndex+1 > m:
        return findmthMin2(left, len(left) + (pivotIndex-m))
    elif pivotIndex+1 < m:
        return findmthMin2(right, m-(pivotIndex+1))


print(findmthMin2([3,-1,-6,7,8,-3,5,1,9,23], 7))
print(findmthMin([3,5,7,1,4], 3))
print(findmthMin([5], 1))
print(findmthMin([-1,2,3], 2))
