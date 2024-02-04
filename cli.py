
while True:
    user_action = input("type,add,edit,show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]
        file = open("todos.txt","r")
        todos = file.readlines()
        file.close()

        todos.append(todo + "\n")

        file = open("todos.txt","w")
        file.writelines(todos)
        file.close()


    elif user_action.startswith('show'):
        file = open("todos.txt","r")
        todos = file.readlines()

        new_todos = [item.strip("\n") for item in todos]

        for index,item in enumerate(new_todos):
            # item = item.strip("\n")
           row = f"{index+1}-{item}"
           print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos[number] = input("edit the todo: ") + "\n"

            file = open("todos.txt","w")
            file.writelines(todos)
            file.close()
        except ValueError:
            print("Enter the number of the todo")
            continue


    elif user_action.startswith('exit'):
        break

print("bye")