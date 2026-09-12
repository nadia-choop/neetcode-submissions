from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []
        for i, j in enumerate(nums):
            diff = target-j
            if diff in hm:
                res.append(hm[diff])
                res.append(i)
                print(res)
                return res
            hm[j] = i    
        