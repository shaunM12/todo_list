tasks = []

def add_one_task(title):
    tasks.append(title)

def print_list():
    starting = 1
    for task in tasks:
        print(starting, task)
        starting += 1

def delete_task(number_to_delete):
    number = number_to_delete - 1
    tasks.pop(number)
    
def save_todos():
    with open("todos.csv", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_todos():
    with open("todos.csv", "r") as file:
        for line in file:
            clean_line = line.strip()
            tasks.append(clean_line)
    
add_one_task("buy milk")
add_one_task("buy eggs")
add_one_task("walk the dog")
add_one_task("mow the lawn")
add_one_task("do the dishes")
add_one_task("wash laundry")

print_list()
# delete_task(2)
# print_list()
save_todos()
load_todos()