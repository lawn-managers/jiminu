import sys

sys.setrecursionlimit(10**6)

def merge(arr1, arr2):
    result = []
    idx1, idx2 = 0, 0
    global count
    while len(arr1) > idx1 and len(arr2) > idx2:
        if arr1[idx1] <= arr2[idx2]:
            result.append(arr1[idx1])
            idx1 += 1
        else :
            result.append(arr2[idx2])
            idx2 += 1

    if idx1 == len(arr1):
        result += arr2[idx2:]
    else:
        result += arr1[idx1:]
        
    count += result
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # WARNING: fucking +1 was problem. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    q = (len(arr)+1) // 2
    left = merge_sort(arr[:q])
    right = merge_sort(arr[q:])
    return merge(left, right)

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = []

merge_sort(arr)

print(-1) if K > len(count) else print(count[K-1])