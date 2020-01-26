def find_majority(arr, n):

    max_count = 0
    index = -1

    # Two Loops for counting the frequency of each element in the array
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1

            if(count > max_count):
                max_count = count
                index = i
    # if max_count is greater than n/2
    if(max_count > n//2):
        print(arr[index])
    else:
        print("There are no majority array")
if __name__=='__main__':
    n = int(input())
    array = list(map(int,input().strip().split()))[:n]
    find_majority(array, n)
