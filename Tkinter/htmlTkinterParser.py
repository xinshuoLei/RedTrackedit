import tkinter as tk
from tk_html_widgets import HTMLLabel
import codecs
f=codecs.open("test.html", 'r')
print(f.read())

root = tk.Tk()
html_label = HTMLLabel(root, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
html_label.pack(fill="both", expand=True)
html_label.fit_height()
html_label2 = HTMLLabel(root, html=f.read())
html_label2.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()
