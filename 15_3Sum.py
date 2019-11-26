class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution_set = []
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            l, r = i + 1, nums_len - 1
            while(l < r):
                sum_val = nums[i] + nums[l] + nums[r]
                if sum_val < 0:
                    l += 1
                elif sum_val > 0:
                    r -= 1
                else:
                    solution = [nums[i], nums[l], nums[r]]
                    l += 1
                    r -= 1
                    need_loop = True
                    while l < r and need_loop:
                        need_loop = False
                        if nums[l] == solution[1]:
                            need_loop = True
                            l += 1
                        if nums[r] == solution[2]:
                            need_loop = True
                            r -= 1
                    #while l < r and nums[r] == solution[2]:
                    #    r -= 1
                    solution_set.append(solution)
            i += 1
            while i < nums_len and nums[i] == nums[i - 1]:
                i += 1
        return solution_set
                