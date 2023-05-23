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
root.tittle("Combobox Example")