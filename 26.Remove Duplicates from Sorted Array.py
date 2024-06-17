''' Given array=[]
we have to remove duplicate data from the array and inplace of that 
var requied = k(no of unique element )(type-list)
              nums(input from the user)(type-list)
              i-iterative var
use of dictionary to store the unique elements with values as the no of repeats
now we have to get the keys from the dic and store back into nums which remove the duplicate items
and return the length as the k (no of unique elements)
              '''
'''def removeDuplicate(nums):
    print(nums)
    dic={}
    len_nums=len(nums)
    for i in range(0,len_nums):
        print(nums[i])
        if nums[i] not in dic:
            dic[nums[i]]=1
        else:
            dic[nums[i]]+=1
    print(dic)
    nums=list(dic.keys())
    print(nums)
    k=len(nums)
    return k

a=removeDuplicate([1,1,2])
print(a) '''

class Solution(object):
    def removeDuplicates(self, nums):
        self.nums=nums
        a=[]
        len_nums=len(nums)
        for i in range(0,len_nums):
            if nums[i] not in a:
                a.append(nums[i])
        #nums=list(dic.keys())
        for i in range(0,len(a)):
            nums[i]=a[i]
        k=len(a)
        for i in range(k,len_nums):
            nums.append('_')
        return k
p=Solution()
a=p.removeDuplicates([-1,0,0,0,0,3,3])
print(a)

'''class Solution(object):
    def removeDuplicates(self, nums):
        self.nums=nums
        a=[]
        dic={}
        len_nums=len(nums)
        for i in range(0,len_nums):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        a=list(dic.keys())
        k=len(a)
        for i in range(0,k):
            nums[i]=a[i]
        for i in range(k,len_nums):
            nums.append('_')
        print(a)
        print(nums)
        return k
p=Solution()
a=p.removeDuplicates([-1,0,0,0,0,3,3])
print(a)'''
        

