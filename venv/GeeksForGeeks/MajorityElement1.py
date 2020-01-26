# Program to find the majority element in the array using hashmap
def find_majority(arr, n):
    m ={}
    # count frequency of each element in the array using hashmap technique
    for i in range(n):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1

    count = 0
    for key in m:
        if m[key] > n/2:
            count = 1
            print ("Majority Found :",key)
            break
    if count ==0 :
        print("No majority Found")

if __name__ == '__main__':
    find_majority([2,2,3,3,3], 5)
