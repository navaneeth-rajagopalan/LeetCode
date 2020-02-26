class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        iterator = 0
        solution = [0] * num_people
        count = 0
        while candies:
            count = (count + 1) if candies > count else candies
            solution[iterator % num_people] += count
            candies -= count
            iterator += 1
        return solution