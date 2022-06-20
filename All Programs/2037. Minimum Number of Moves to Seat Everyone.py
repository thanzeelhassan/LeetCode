class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            result = result + abs(seats[i] - students[i])
        return result
