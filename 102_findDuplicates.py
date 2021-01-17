class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
        
        # ----------------------
        
        j=0
        for i in range(len(nums)):
            while nums[nums[j]-1] != nums[j]:
                nums[nums[j]-1], nums[j] = nums[j], nums[nums[j]-1]
            j+=1
        print(nums)
        res = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                res.append(nums[i])
        return res
            
