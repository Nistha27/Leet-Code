'''You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.'''

'''Explanation
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.'''

'''def unique(nums):
    unique=[]
    moves=0
    nums.sort()
    #print("nums_list",nums)
    for i in range(len(nums)):
        #print("nums[i={}]:{}".format(i,nums[i]))
        unique.append(nums[i])
        #print("unique_list:",unique)
        for j in range(i,len(nums)):
            #print("j",j)
            while(nums[j] in unique):
                #print("nums[j={}]:{}".format(j,nums[j]))
                nums[j]+=1
                moves+=1
                #print("new_nums[j={}]:{},moves:{}".format(j,nums[j],moves))
    print(int(moves/2))
    print(unique)'''
'''class Solution(object):
    def minIncrementForUnique(self,nums):
        self.nums=nums
        unique= {}
        move = 0
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if str(nums[i]) in unique.keys():
                move = move+1
                unique[str(nums[i]+1)] = 1
            else:
                unique[str(str(nums[i]))] = 1
        print(unique)
        return move'''
        


'''class Solution(object):
    def minIncrementForUnique(self,nums):
        self.nums=nums
        unique = {}
        move = 0
        nums.sort()
        print(f"L :{nums}")
        for i in range(len(nums)):
            print(f"step: {i}")
            if str(nums[i]) in unique.keys():
                print(f"......IF : {nums[i]}")
                m = nums[i]
                while (str(m) in unique.keys() ):
                    move = move+1
                    m = m+1
                unique[str(m)] = 1
            else:
                print(f"......ELSE : {nums[i]}")
                nums[str(str(nums[i]))] = 1
        print(f"----unique : {unique}")
        print(f"unique:{unique}")
        print(f"move : {move}")
        
p=Solution()
a=p.minIncrementForUnique([3,2,1,2,1,7])
print("a",a)'''

class Solution(object):
    def minIncrementForUnique(self, nums):
        self.nums = nums
        nums.sort()
        move = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                inc = nums[i - 1] - nums[i] + 1
                move += inc
                nums[i] += inc

        return move
nums=[1,2,2]

