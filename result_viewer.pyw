from tkinterweb import HtmlFrame
from tkinter import *
import os

os.system("TASKKILL /F /IM cmd.exe")

root = Tk()
root.title("Results")
frame = HtmlFrame(root)
frame.load_website(r"http://127.0.0.1:5000/")
frame.pack(fill="both", expand=True)
Button(root, text="Back", command=lambda: quit()).pack()
root.mainloop()