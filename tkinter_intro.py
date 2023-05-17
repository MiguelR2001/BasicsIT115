#Importing the tkinter library.
import tkinter as tk


#Creates function for when button is clicked.
def button_click():
    print("Button Clicked!")


#Creates parent window or root window.
root = tk.Tk()
root.title("Button Example")

#Creates button with 3 parameters; class library, text, function call.
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#Creates mainloop to keep the root window open.
root.mainloop()
