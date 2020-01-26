def printLeaders(arr, size):
    max_right_array = arr[size - 1]
    print (max_right_array,)
    for i in range(size-2, -1,-1):
        if max_right_array < arr[i]:
            print(arr[i],)
            max_right_array = arr[i]
if __name__=='__main__':
    n = int(input())
    array = list(map(int, input().strip().split()))[:n]
    printLeaders(array, n)