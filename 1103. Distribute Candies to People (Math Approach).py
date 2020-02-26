import math

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        pseudo_num_people = (-1 + math.sqrt(8*candies)) // 2
        num_rounds = int(pseudo_num_people // num_people)
        remaining = int(pseudo_num_people % num_people)        
        solution = [0] * num_people
        
        for i in range(1, num_people + 1):
            rounds_encountered = num_rounds + 1 if i <= remaining else num_rounds            
            solution[i - 1] = int((rounds_encountered * i) + ((rounds_encountered - 1) * rounds_encountered / 2) * num_people)            
        solution[remaining] += int(candies - (pseudo_num_people * (pseudo_num_people + 1) / 2))
        return solution