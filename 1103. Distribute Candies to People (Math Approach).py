import math

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        pseudo_num_people = (-1 + math.sqrt(8*candies)) // 2
        num_rounds = int(pseudo_num_people // num_people)
        remaining = int(pseudo_num_people % num_people)        
        solution = [0] * num_people
        
        for i in range(1, num_people + 1):
            solution[i - 1] = sum([(i + j*num_people) for j in range(num_rounds + 1 if i <= remaining else num_rounds)])
        solution[remaining] += int(candies - (pseudo_num_people * (pseudo_num_people + 1) / 2))
        return solution