# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 == 0:
        return numbers
    else:
        num = numbers[len(numbers) - 1] + 1
        numbers.append(num)
        add_numbers_to_list(numbers)

if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)