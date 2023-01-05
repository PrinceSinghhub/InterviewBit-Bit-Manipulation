class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        l=len(A)
        ans=0
        for i in range(31):
            count1=0
            for a in A:
                if a&(1<<i)>0:
                    count1+=1
            ans+=2*count1*(l-count1)
        return ans%1000000007


ans = Solution()
A=[1, 3, 5]
print(ans.cntBits(A))