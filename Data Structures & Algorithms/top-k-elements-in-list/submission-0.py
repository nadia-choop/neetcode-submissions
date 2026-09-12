class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top = count.most_common(k)
        result = []
        for (i, j) in top:
            result.append(i)
        return result