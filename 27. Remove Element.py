class Solution(object):
    def removeElement(nums,val):
        a=[]
        len_nums=len(nums)
        for i in range(0,len_nums):
            if(nums[i]!=val):
                a.append(nums[i])
        k=len(a)
        for i in range(len(a),len_nums):
            a.append('_')
        for i in range(0,len(a)):
            nums[i]=a[i]
        return k
p=Solution
ans=p.removeElement([3,2,2,3],3)
print(ans)