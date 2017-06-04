
nums = [2,4,6,8,3,2,56,8,7,2,3,5,7,3,2,5,7,8,3,2,3,2,1,4,6,8]
target = 9

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j] == target):
            print ([i,j])
            break