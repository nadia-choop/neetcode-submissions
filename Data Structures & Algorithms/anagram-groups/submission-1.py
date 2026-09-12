class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in tracker:
                ind = tracker[s_sorted]
                res[ind].append(s)
            else:
                res.append([s])
                tracker[s_sorted] = len(tracker)
        return res
        