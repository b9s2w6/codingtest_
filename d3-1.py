T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    building = int(input())
    height = list()
    index = [-2, -1, 1, 2]
    sum = 0
    height = list(map(int, input().split()))
    for i in range(2, building-2):
        if height[i-1] < height[i] and height[i-2] < height[i]:
            if height[i+1] < height[i] and height[i+2] < height[i]:
                max_ = -1
                for j in range(4):
                    if max_ < height[i+index[j]]:
                        max_ = height[i+index[j]]
                sum += height[i] - max_
    print("#%d %d"%(test_case, sum))