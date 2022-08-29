def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        arr_bin = format(arr1[i]|arr2[i], 'b') 
        print(arr_bin)
        table = str.maketrans('01', ' #')
        answer.append(arr_bin.zfill(n).translate(table))
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


print(solution(n,arr1, arr2))