'''Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.'''

'''
Input: hours = [12,12,30,24,24]

Output: 2

Explanation: The pairs of indices that form a complete day are (0, 1) and (3, 4).

Example 2:

Input: hours = [72,48,24,3]

Output: 3

Explanation: The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).'''

'''
use of mod (%) 24'''


'''
input=[12,12,30,24,24]

input=[72,48,24,3]
'''

    
def day(hours):
    count=0
    for i in range(len(hours)-1,-1,-1):
        if(hours[i]%24==0):
            count+=1
        if((hours[i]+hours[i+1])%24==0):
            count+=1
    return count

input=[72,48,24,3]
days=day(input)
print(days)



    