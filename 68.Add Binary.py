'''Binary addition
a=1001
b=001
adding zero to the left of the str  if len(a)!=len(b) 
no of variable requires 
carry,sum,res
No of condtions for addtion
0+0=0,carry=0
0+1=1,carry=0
1+0=1,carry=0
1+1=0,carry=1
'''
class Solution(object):
    def addBinary(self,a,b):
        self.a=a
        self.b=b
        res=''
        a=list(a[::-1])
        b=list(b[::-1])
        print("a:",a)
        print("b:",b)
        carry=0
        sum=[]
        if(len(a)>len(b)):
            for i in range(len(b),len(a)+1):
                b.insert(i,'0')
        elif(len(b)>len(a)):
            for i in range(len(a),len(b)):
                a.insert(i,'0')
        print("a_rev:",a)
        print("b_rev:",b)
        for i in range(len(a)):
            print("a",a[i])
            print("b",b[i])
            if(int(a[i])+int(b[i])+carry==0):
                sum.insert(i,0)
                carry=0
            elif(int(a[i])+int(b[i])+carry==1):
                sum.insert(i,1)
                carry=0
            elif(int(a[i])+int(b[i])+carry==2):
                sum.insert(i,0)
                carry=1
            elif(int(a[i])+int(b[i])+carry==3):
                sum.insert(i,1)
                carry=1
            print("sum:",sum[i])
            print("carry:",carry)
        if(carry==1):
            sum.insert(i+1,1)
        sum=sum[::-1]
        for i in range(len(sum)):
            res=res+str(sum[i])
        return res

res = Solution()
p=res.addBinary("1","111")
print(p)   