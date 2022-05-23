def twosum(arr,target_sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>target_sum):
            right=right-1
        elif(arr[left]+arr[right]<target_sum):
            left=left+1
        elif(arr[left]+arr[right]==target_sum):
                print("values of pair are [",arr.index(arr[left]),",",arr.index(arr[right]),"]","[",arr.index(arr[right]),",",arr.index(arr[left]),"]")
                right=right-1
                left=left+1
arr=[10,20,10,40,50,60,70]
target_sum=50
twosum(arr,target_sum)
