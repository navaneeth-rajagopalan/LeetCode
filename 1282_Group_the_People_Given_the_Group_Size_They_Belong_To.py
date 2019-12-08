class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        res = []
        for i, grp_sz in enumerate(groupSizes):
            groups[grp_sz].append(i)
        return [lst[i: i + s] for s, lst in groups.items() for i in range(0, len(lst), s)]
        