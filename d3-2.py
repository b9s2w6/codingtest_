T = int(input())

for test_case in range(1, T + 1):
    money, change = map(int, input().split())
    money_str = str(money)
    money_list = list()
    for i in range(len(money_str)):
        money_list.append(int(money_str[i]))
    cp_money_list = money_list[:]
    cp_money_list.sort(reverse=True)

    for i in range(change):
        max = -1
        max_index = -1
        d = 0
        for j in range(len(money_list)):
            if j == len(money_list) -1:
                d = j
            elif cp_money_list[j] == money_list[j]:
                pass
            else:
                d = j
                break

        for j in range(d, len(money_list)):
            if d == len(money_list)-1:
                max_index = d-1
            else :
                if max <= money_list[j]:
                elif max <= money_list[j]:
                    max = money_list[j]
                    max_index = j
        money_list[d], money_list[max_index] = money_list[max_index], money_list[d]

    num = ''
    for i in range(len(money_list)):
        num += str(money_list[i])
    num = int(num)
    print("#%d %d" % (test_case, num))