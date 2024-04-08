# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    count = 0

    def __init__(self, week: int, list: list):
        self.week = week
        self.list = list

    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.list])

    def hits_in_place(self, numbers):
        return [num if num in self.list else -1 for num in numbers]

if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))