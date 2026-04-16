class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)>>1
            cnt=0
            for i in nums:
                if i <= mid:
                    cnt+=1
            if cnt>mid:
                ans=mid
                r=mid-1
            else:
                l=mid+1 
        return ans
        
        