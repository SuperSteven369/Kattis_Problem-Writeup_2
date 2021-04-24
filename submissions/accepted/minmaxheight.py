#!/usr/bin/env python3
T = int(input())
for i in range(T):
    n = int(input())
    res = [0] * n
    height = [int(ele) for ele in input().split()]
    height.sort()
    k = 0
    for j in range(n):
        if not (j + 1) % 2:
            res[k] = height[j]
            k += 1
    for j in reversed(range(n)):
        if (j + 1) % 2:
            res[k] = height[j]
            k += 1
    diff = abs(res[0] - res[1])
    for j in range(2, k):
        diff = max(diff, abs(res[j] - res[j - 1]))
    print(diff)
