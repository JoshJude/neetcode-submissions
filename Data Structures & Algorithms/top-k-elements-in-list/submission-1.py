class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            seen[n] = 1 + seen.get(n, 0)

        freq = [[] for i in range(0, len(nums) + 1)]

        for s in seen:
            freq[seen[s]].append(s)

        top = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                top.append(n)

                if len(top) == k:
                    return top