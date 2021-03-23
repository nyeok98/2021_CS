def binary_search(ar, target):
    first = 0
    last = len(ar)-1
    mid = 0

    while first<=last:
        mid = (first+last)//2
        if ar[mid] == target:
            return mid
        elif ar[mid] > target:
            last = mid-1
        else:
            first = mid+1

    return -1

m = [7, 19, 21, 25, 27, 30, 32, 32, 37, 47, 53, 92, 94, 98]
print(binary_search(m,27))