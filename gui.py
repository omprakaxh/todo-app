import PySimpleGUI as sg
import function

label = sg.Text("Type a Todo")
text_box = sg.InputText(tooltip="Enter a todo",key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(function.get_todos(),key="todos",
                      enable_events=True, size= [40, 10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [text_box,add_button],
                           [list_box,edit_button,delete_button],
                           [exit_button]] ,
                   font=("Helvetica",20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window["todos"].update(values=todos)
        case "Delete":
            todo_to_delete = values["todos"][0]
            todos = function.get_todos()
            todos.remove(todo_to_delete)
            function.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
