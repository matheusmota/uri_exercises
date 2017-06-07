nums = [int(i) for i in input().split()]
originalNums = nums.copy()
for i, num in enumerate(nums):
        for j, numj in enumerate(nums):
            if(num < numj):
                aux = numj
                nums[j] = nums[i]
                nums[i] = aux
                
                

print(nums[0])
print(nums[1])
print(nums[2])
print()
print(originalNums[0])
print(originalNums[1])
print(originalNums[2])
