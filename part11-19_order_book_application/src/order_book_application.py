# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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
        try:
            for order in self.Orders:
                if order.id == id:
                    order.mark_finished()
                    return True
        
            return False
        except ValueError:
            print("erroneous input")
    
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
            return None

        return (num_finished, num_unfinished, sum_finished_workload, sum_unfinished_workload)

def command_list():
    print(f"commands:")
    print("0 exit")
    print(f"1 add order")
    print(f"2 list finished tasks")
    print(f"3 list unfinished tasks")
    print(f"4 mark task as finished")
    print(f"5 programmers")
    print(f"6 status of programmer")

orders = OrderBook()
command_list()
command_input = int(input("command: "))

while command_input != 0:
    if command_input == 1:
        description_input = input("description: ")
        programmer_workload_input = input("programmer and workload estimate: ")
        programmer_workload = programmer_workload_input.split(' ')
        try:
            try:
                programmer_workload_hours = int(programmer_workload[1])
                orders.add_order(description_input, programmer_workload[0], int(programmer_workload_hours))
                print("added!")
            except ValueError:
                print("erroneous input")
        except IndexError:
            print("erroneous input")

    elif command_input == 2:
        if len(orders.finished_orders()) == 0:
            print("no finished tasks")
        
        for order in orders.finished_orders():
            print(order)

    elif command_input == 3:
        if len(orders.unfinished_orders()) == 0:
            print("no unfinished tasks")

        for order in orders.unfinished_orders():
            print(order)

    elif command_input == 4:
        try:
            id_input = int(input("id: "))
            result = orders.mark_finished(id_input)
            if result is None:
                print("erroneous input")
            elif result == True:
                print("marked as finished")
            else:
                print("erroneous input")
        except ValueError:
            print("erroneous input")

    elif command_input == 5:
        for name in orders.programmers():
            print(name)

    elif command_input == 6:
        name_input = input("programmer: ")
        programmer_status = orders.status_of_programmer(name_input)
        if programmer_status == None:
            print("erroneous input")
        else:
            print(f"tasks: finished {programmer_status[0]} not finished {programmer_status[1]}, hours: done {programmer_status[2]} scheduled {programmer_status[3]}")

    command_input = int(input("command: "))