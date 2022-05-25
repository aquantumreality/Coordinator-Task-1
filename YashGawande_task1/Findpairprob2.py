class findpair:
    nums = [10,20,10,40,50,60,70]
    target = int(input("Enter target Number: "))
    dict = {}
    pair_number = 0
    # consider each element except the last
    for i in range(0,len(nums)-1):
 
        # start from the first element until the last element
        for j in range(0, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                pair_number+=1
                dict.update({pair_number:[i,j]})

    print(dict)
