# Write your solution here:
class Task:
    id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = 'NOT FINISHED'
        self.id = Task.id_counter
        Task.id_counter += 1

    def is_finished(self):
        if self.finished == 'FINISHED':
            return True
        
        return False
    
    def mark_finished(self):
        self.finished = 'FINISHED'

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}'

class OrderBook:

    def __init__(self):
        self.Orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        new_order = Task(description, programmer, workload)
        self.Orders.append(new_order)

    def all_orders(self):
        return self.Orders

    def programmers(self):
        names = []
        for i in range(len(self.Orders)):
            names.append(self.Orders[i].programmer)
        
        return list(set(names))
    
    def mark_finished(self, id: int):
        for order in self.Orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("No order with the given id.")
    
    def finished_orders(self):
        return [order for order in self.Orders if order.is_finished() == True]

    def unfinished_orders(self):
        return [order for order in self.Orders if order.is_finished() == False]

    def status_of_programmer(self, programmer: str):
        num_finished = 0
        num_unfinished = 0
        sum_unfinished_workload = 0
        sum_finished_workload = 0

        for person in self.Orders:
            if person.programmer == programmer:
                if person.is_finished() == True:
                    sum_finished_workload += person.workload
                    num_finished += 1
                else:
                    sum_unfinished_workload += person.workload
                    num_unfinished += 1

        if num_finished == 0 and num_unfinished == 0:
            raise ValueError(f"No tasks found for the programmer: {programmer}")

        return (num_finished, num_unfinished, sum_finished_workload, sum_unfinished_workload)
                
if __name__ == "__main__":
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.status_of_programmer("JohnDoe")
    