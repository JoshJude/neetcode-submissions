class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            seen[n] = seen[n] + 1 if n in seen else 1

        return sorted(seen, key=seen.get, reverse=True)[:k]