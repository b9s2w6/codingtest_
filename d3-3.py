T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())
    boxList = list(map(int, input().split()))

    for i in range(dump):
        max_ = 0
        min_ = 0
        for j in range(len(boxList)):
            if boxList[max_] < boxList[j]:
                max_ = j
            if boxList[min_] > boxList[j]:
                min_ = j
        boxList[max_] -= 1
        boxList[min_] += 1
    max_ = 0
    min_ = 101
    for j in range(len(boxList)):
        if boxList[max_] < boxList[j]:
            max_ = j
        if boxList[min_] > boxList[j]:
            min_ = j

    print("#%d %d" % (test_case, boxList[max_] - boxList[min_]))