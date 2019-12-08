import tkinter as tk
from PIL import Image

from autonomousPRAW import redditToCSV

from tk_html_widgets import HTMLLabel

HEIGHT = 500
WIDTH = 600
htmlString = ""
def get_subreddit(entry):
    try:
        htmlString = redditToCSV(entry)
        print("Scraped data from r/", entry)
        #htmlLabel.set_html(htmlString, strip=True)
        #print(htmlString)
        print("Finished, html loaded")
    except Exception:
        print("Sorry, this is not a real subreddit/ Try again")
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#insert own path to background image
background = tk.PhotoImage(file = 'reddit-wide.png')
background_label = tk.Label(root, image = background)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg='#DA826F', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

#editable text box
entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get subreddit data", font = 40, command=lambda: get_subreddit(entry.get()))
button.place(relx = 0.7, rely = 0.1, relwidth = 0.25, relheight = 0.3)
"""
lower_frame = tk.Frame(root, bg='#DA826F', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor = 'n')

htmlLabel = HTMLLabel(lower_frame)
htmlLabel.set_html("<html></html>", strip=True)
htmlLabel.place(relwidth = 1, relheight = 1)
"""
root.mainloop()
