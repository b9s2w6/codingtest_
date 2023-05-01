from typing import List

T = int(input())

for test_case in range(1, T + 1):
    code_dict = {'0001101' : '0', '0011001':'1', '0010011' : '2', '0111101' : '3', '0100011' : '4', '0110001' : '5', '0101111' : '6', '0111011': '7', '0110111':'8', '0001011':'9'}
    n, m = map(int, input().split())
    code = [['0']*m for _ in range(n)]
    #n_, m_ = 0, 0
    n_, m_ = n-1, m-1
    for i in range(n) :
            code[i] = list(input())
    a = '' #코드 8bit 찾기
    b = '' #찾은 코드 문자화하는 변수
    flag = False #2중for문 break 용도

    while code[n_][m_] == '0':
        if m_-1 == -1:
            n_-=1
            m_=m-1
        else : m_-=1
    code_list = list()
    for i in range(56):
        code_list.append(code[n_][m_])
        if i == 55:
            break
        m_-=1
        if m_ == -1:
            n_ -= 1
            m_ = m - 1
    while code_list:
        rev_code_list = code_list.pop()

    code_str = ''
    code_int = list()

    for i in range(m_, m_ + 56, 7):
        code_str = ''
        for j in range(7):
            code_str += code[n_][i + j]
        code_int.append(code_dict[code_str])

    even = 0
    odd = 0

    for i in range(8):
        if (i+1) % 2 == 1:
            odd+=int(code_int[i])
        else : even+=int(code_int[i])
    text = odd*3+even
    if text % 10 == 0:
        sum = even+odd
        print("#%d %d"%(test_case, sum))
    else: print("#%d 0"%(test_case))

"""
    for i in range(n):
        for j in range(m-7):
            a = code[i][j:j+7]
            b = ''
            for k in range(7):
                b += a[k]
            if b in code_dict:
                n_ = i
                m_ = j
                flag = True
                break
        if flag:
            break
            
    code_str = ''
"""