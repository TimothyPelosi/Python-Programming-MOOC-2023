class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def order_by_length(route: tuple):
    return route.length

def sort_by_length(routes: list):
    return sorted(routes, key=order_by_length, reverse=True)

def order_by_difficulty(route: tuple):
    return (route.grade, route.length)

def sort_by_difficulty(routes:list):
    return sorted(routes, key=order_by_difficulty, reverse=True)
    

    

# Write your solution herer:

if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])

    for route in sort_by_difficulty(reply):
        print(route)