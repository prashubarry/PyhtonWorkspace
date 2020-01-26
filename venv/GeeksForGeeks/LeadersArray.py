def printLeaders(arr, size):
    for i in range(size):
        for j in range(i+1,size):
            if(arr[i]<=arr[j]):
                break
        if(j==size-1):
            print(arr[i],)
if __name__=='__main__':
    n = int(input())
    array = list(map(int,input().strip().split()))[:n]
    printLeaders(array, n)