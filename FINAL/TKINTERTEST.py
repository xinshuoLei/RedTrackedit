import tkinter as tk

root = tk.Tk()

booleanA = True

def newFunctionThingy(booleanA):
    print("HI")
    if (booleanA):
        booleanA = False
        str1 = "B"
    else:
        booleanA = True
        str1 = "A"
    label.config(text=str1)
button = tk.Button(root, command = lambda: newFunctionThingy(booleanA), height = 50, width = 50)
button.place(relx = 0.7, rely = 0.1)
str1 = "A"

label = tk.Label(root, text = str1)
label.pack()

root.mainloop()
