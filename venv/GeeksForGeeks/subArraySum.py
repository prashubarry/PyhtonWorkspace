def subArraySum(arr, n, sum):
    for i in range(n):

        curr_sum = arr[i]

        j = i + 1

        # Iterate through all the elements of the array
        while j <= n:

            if curr_sum == sum:
                print("Sum found between")
                print("indexes %d and %d" % (i, j - 1))
                return 1

            if curr_sum > sum and j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print("No Subarray Found")
    return 0


if __name__ == '__main__':
    n = int(input())

    input_arr = list(map(int, input().strip().split()))[:n]

    sum = int(input())

    print(subArraySum(input_arr, n, sum))
