class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = []
        for i in range(1 << len(nums)):
            subset = []
            for ii in range(len(nums)):
                if (i >> ii) & 1:
                    subset.append(nums[ii])
            res.append(subset)
        return res

        """
        For a list with a length n, say [1, 2, 3] with a length 3, 
        we have 2 ** n combinations (for an element can be selected or not selected). 
        Therefore, the time complexity would be O(2 ** n).
        We need to traverse through these 2 ** n subsets.
        
        Consider, for [1, 2, 3], the combination could be these 8:
        000
        001
        010
        011
        100
        101
        110
        111
        
        This is actually the answer. All we need to do is map these bits 
        to the results.  
        """


if __name__ == "__main__":
    solution = Solution()
    l = [1, 2, 3, 4, 5]
    res = solution.subsets(l)
    print(res)
