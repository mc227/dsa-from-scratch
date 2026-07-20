# nums = [2,7,11,15]
# target = 9
# # return [0,1]


# for i in range(len(nums)-1):
#     for j in range(1,len(nums)):
#         if nums[i] != nums[j] and nums[i] < nums[j]:
#             if nums[i] + nums[j] == target:
#                 print(i,j)

nums = [3,3]
target = 6
# return [0,1]


for i in range(len(nums)-1):
    for j in range(1,len(nums)):
        if nums[i] != nums[j] and nums[i] < nums[j]:
            if nums[i] + nums[j] == target:
                print(i,j)
        else:
            if nums[i] + nums[j] == target:
                print(i,j)
