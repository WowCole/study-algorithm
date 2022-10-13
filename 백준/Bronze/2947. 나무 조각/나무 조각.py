nums = list(map(int,input().split()))

while nums != sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            print(" ".join(map(str,nums)))