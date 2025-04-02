class Solution(object):
    def plusOne(self, digits):
        self.digits=digits
        new=0
        new_list=[]
        digits=digits[::-1]
        for i in range(len(digits)):
            new=new+digits[i]*pow(10,i)
        new=new+1
        new=str(new)
        for i in new:
            new_list.append(int(i))
        return new_list
        