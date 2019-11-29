import tkinter as tk #Used for all GUI generation
from tk_html_widgets import HTMLLabel #Allows for parsing of HTML in GUI
import codecs #Reads files

# Takes a path and reads HTML
# path -> The path where the HTML file should be found
# RETURNS -> A string representing the HTML in the file
def readHTML(path):
	f=codecs.open(path, 'r')
	return f.read()


# Creates an html label object using a rootview and the parsed html
# rootView -> tk.Tk() object to display HTML on
# htmlAsString -> HTML parsed as a string to be loaded
# RETURNS -> Tkinter object that still needs to be packed and have other variable settings applied (this is so someone else can determine order in which HTML files are applied to root)
def generateLabel(rootView, htmlAsString):
	html_label = HTMLLabel(rootView, html = htmlAsString)
	return html_label

#Example code showing how to use wrapper functions
def example():
	root = tk.Tk()
	element = generateLabel(root, readHTML("test.html"))
	element.pack()
	root.mainloop

example()
