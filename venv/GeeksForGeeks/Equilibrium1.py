def equilibrium(arr, n):
    for i in range(n):

        leftSum = 0
        rightSum = 0

        for j in range(i):
            leftSum+=arr[j]

        for j in range(i+1, n):
            rightSum+=arr[j]

        if leftSum==rightSum:
            return i

    return -1

if __name__=='__main__':
    n = int(input())
    array = list(map(int, input().strip().split()))[:n]
    print(equilibrium(array, n))