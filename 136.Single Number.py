'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 '''





class Solution(object):
    def singleNumber(self, nums):
        self.nums=nums
        dict_nums={}
        for i in range(len(nums)):
            if(nums[i] not in dict_nums):
                dict_nums[nums[i]]=1
            else:
                dict_nums[nums[i]]+=1
        print(dict_nums)
        for keys,values in dict_nums.items():
            if(values==1):
                return keys
            
p=Solution()
a=p.singleNumber([4,1,2,1,2])
print(a)