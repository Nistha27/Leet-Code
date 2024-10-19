'''You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.'''

'''Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5

Explanation:

step	nums	averages
0	[7,8,3,4,15,13,4,1]	[]
1	[7,8,3,4,13,4]	[8]
2	[7,8,4,4]	[8,8]
3	[7,4]	[8,8,6]
4	[]	[8,8,6,5.5]The smallest element of averages, 5.5, is returned.
Example 2:

Input: nums = [1,9,8,3,10,5]

Output: 5.5

Explanation:

step	nums	averages
0	[1,9,8,3,10,5]	[]
1	[9,8,3,5]	[5.5]
2	[8,5]	[5.5,6]
3	[]	[5.5,6,6.5]
Example 3:

Input: nums = [1,2,3,7,8,9]

Output: 5.0

Explanation:

step	nums	averages
0	[1,2,3,7,8,9]	[]
1	[2,3,7,8]	[5]
2	[3,7]	[5,5]
3	[]	[5,5,5]'''

'''def min_(nums):
    average=[]
    n=int(len(nums)/2)
    for i in range(n):
        print(i)
        min_element=min(nums)
        max_element=max(nums)
        average_element=(min_element+max_element)/2
        nums.remove(min_element)
        nums.remove(max_element)
        average.append(average_element)

    a=min(average)
    return(a)'''
    



'''class Solution(object):
    def minimumAverage(self, nums):
        self.nums=nums
        average=[]
        n=int(len(nums)/2)
        for i in range(n):
            min_element=min(nums)
            max_element=max(nums)
            average_element=(min_element+max_element)/2
            nums.remove(min_element)
            nums.remove(max_element)
            average.append(average_element)

        a=min(average)
        return(a)
p=Solution()
a=p.minimumAverage([7,8,3,4,15,13,4,1])
print(a)'''

'''def min_avg(nums):
    # Sort the input array
    nums.sort()
    
    # Initialize an empty list for averages
    averages = []
    
    # Determine the number of iterations
    num_iterations = len(nums) // 2
    
    # Iterate n / 2 times
    for _ in range(num_iterations):
        # Remove the smallest and largest elements
        minElement = nums.pop(0)
        maxElement = nums.pop(-1)
        
        # Calculate the average and add to averages list
        average_value = (minElement + maxElement) / 2
        averages.append(average_value)
    
    # Find the minimum element in averages
    min_average = min(averages)
    
    return min_average'''

class Solution(object):
    def minimumAverage(self, nums):
        self.nums=nums
        nums.sort()
        averages = []
        num_iterations = len(nums) // 2
        for _ in range(num_iterations):
            minElement = nums.pop(0)
            maxElement = nums.pop(-1)
            average_value = (minElement + maxElement) / 2
            averages.append(average_value)

        min_average = min(averages)
        return min_average

p=Solution()
a=p.minimumAverage([1,2,3,7,8,9])
print(a)





    
