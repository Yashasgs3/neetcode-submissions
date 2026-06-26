class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #create a empty dictionary
        count = {}
       # take 1 num at a time from nums list and then append to count dictionary
        for num in nums:
            count[num] = count.get(num,0) + 1
       # create a frequency hashmap bucket for range 0 to len(nums)
        freq = [[] for _ in range(len(nums)+1)]
       #count values using c for count of number times each num has occured and append to freq hashmap
        for num,c in count.items():
            freq[c].append(num)
       # create answer
        res = []
        for i in range(len(freq)-1,0,-1): # we will start from the highest frequency
               for num in freq[i]:
                 res.append(num)

                 if len(res) == k:
                    return res
