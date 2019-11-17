import tkinter as tk

HEIGHT = 500
WIDTH = 600

def get_subreddit(entry):
    print("Scraping data from r/", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background = tk.PhotoImage(file = '/Users/albert/Documents/reddit-wallpaper-full-hd-1080p-83752.jpg')
#backgroun_label = tk.Label(root, image = background)
#background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg='#DA826F', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

#editable text box
entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get subreddit data", font = 40, command=lambda: get_subreddit(entry.get()))
button.place(relx = 0.7, rely = 0.1, relwidth = 0.25, relheight = 0.3)

lower_frame = tk.Frame(root, bg='#DA826F', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor = 'n')

label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)


root.mainloop()
