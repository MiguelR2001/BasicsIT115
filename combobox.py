#Importing the class library.
import tkinter as tk
from tkinter import ttk


#Defines a function called on_select that takes an event parameter.
def on_select(event):

    #Creates an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Tkinter GUI application window and setting its title.
root = tk.Tk()
root.title("Combobox Example")


#Creates an array of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#
combo_box = ttk.Combobox(root, values=items)
#Binding the on_select function.
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

root.mainloop()