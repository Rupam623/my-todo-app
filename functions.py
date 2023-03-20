FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath) as file:
        todos1 = file.readlines()
        return todos1

def write_todos(todos2, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos2)
