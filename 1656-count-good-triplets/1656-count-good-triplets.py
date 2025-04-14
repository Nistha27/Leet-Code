class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        #Time Complexity : O(N^3)
        #Brute Force
        count=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j])<=a and abs(arr[k]-arr[j])<=b and abs(arr[i]-arr[k])<=c:
                        count+=1
        return count


        
        