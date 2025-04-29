class Solution(object):
    def countSubarrays(self, nums, k):
        #Optimized
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window >= k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans


        '''Brute Force
        count=0
        n=len(nums)
        maxelem=max(nums)
        for i in range(n):
            for j in range(i,n):
                new_arr=nums[i:j+1]
                count_elem=Counter(new_arr)
                print(new_arr)
                if count_elem[maxelem]>=k:
                    count+=1
        return count'''
            

            

        
        