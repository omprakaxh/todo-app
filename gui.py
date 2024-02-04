import PySimpleGUI as sg

label = sg.Text("Type a Todo")
text_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',layout=[[label], [text_box,add_button]])
window.read()
window.close()
