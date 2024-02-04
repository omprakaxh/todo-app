FILEPATH =  "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as filelocal:
        todos_local = filelocal.readlines()
    return todos_local
def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

