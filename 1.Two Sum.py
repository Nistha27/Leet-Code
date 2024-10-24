''' Two input variables num and target 
num - array/list type
target-int type
res =list type (return variable)
array has exactly one solution
return the index position of the numbers in the form of a list'''


class Solution(object):

    def twosum(self,nums,target):
        self.nums=nums
        self.target=target
        res=[]
        len_nums=len(nums)
        for i in range(0,len_nums):
            for j in range(i+1,len_nums):
                if(nums[i]+nums[j]==target):
                    print(nums[i])
                    print(nums[j])
                    res.append(i)
                    res.append(j)
                    return res

a=Solution()
z=a.twosum([2,5,5,3],10)
print(z)