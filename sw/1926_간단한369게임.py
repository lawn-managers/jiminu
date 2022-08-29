T = int(input())
answer = ''

for test_case in range(1, T + 1) :
    if '3' in str(test_case) or '6' in str(test_case) or '9' in str(test_case) :
        for i in range(0, len(str(test_case))) :
            if str(test_case)[i] == '3' or str(test_case)[i] == '6' or str(test_case)[i] == '9':
                answer += '-'
        answer += ' '
    else :
        answer += str(test_case) + ' '
print(answer)