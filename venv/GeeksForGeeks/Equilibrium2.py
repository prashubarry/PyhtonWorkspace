def equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num

        if left_sum == total_sum:
            return i
        left_sum += num
    return -1


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().strip().split()))[:n]
    print(equilibrium(array))
