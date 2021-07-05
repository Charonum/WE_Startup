import time
import webbrowser
from tkinter import *
import os

import wget
from bs4 import BeautifulSoup


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def search_result_manage(se):
    u = se.replace(" ", "+")
    wget.download(f"https://www.info.com/serp?q={u}", "tmp.html")
    with open("tmp.html") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
    os.remove("tmp.html")
    ree = soup.find('div', class_='web-bing')
    try:
        s = open(r"templates\results.html", "r+")
        s.seek(0)
        s.truncate()
    except:
        s = open(r"templates\results.html", "w")
    s.write(ree.prettify())


res = ""


def search(se):
    global res
    if se.get() == "":
        pass
    else:
        try:
            search_result_manage(se.get())
            result()
        except:
            Label(root, text="Oh No! We ran into an error. Please search again.", foreground="red").pack()


def result():
    webbrowser.open(r"templates\results.html")


def clo():
    os.system("TASKKILL /F /IM python.exe")
    os.system("TASKKILL /F /IM pythonw.exe")


def sa(maxi, ad):
    print(maxi.get())
    print(ad.get())


def s():
    root = Toplevel()
    root.title("Settings")
    root.geometry("500x600")
    ss = open("settings.txt")
    cms, cab = ss.read().split("\n")
    Label(root, text="Settings", font=("Arial", 25, "bold")).pack()
    Label(root).pack()
    is_on = None

    # Create Label
    my_label = Label(root,
                     text="The Switch Is On",
                     fg="green",
                     font=("Helvetica", 32))

    my_label.pack(pady=20)

    def switch(is_on):
        if is_on:
            on_button.config(image=off)
            my_label.config(text="The Switch is Off", fg="grey")
            is_on = False
        else:
            on_button.config(image=on)
            my_label.config(text="The Switch is On", fg="green")
            is_on = True

    on = PhotoImage(file="on.png")
    off = PhotoImage(file="off.png")

    on_button = Button(root, image=on, bd=0, command=lambda: switch(is_on))
    on_button.pack(pady=50)
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    Label(root).pack()
    # Button(root, text="Save", command=lambda: sa(ms, ab)).pack()
    root.mainloop()


root = Tk()
root.protocol("WM_DELETE_WINDOW", clo)
root.geometry("1920x1080")
root.state('zoomed')
# image = PhotoImage(file='settings.png')
# photo = image.subsample(30, 30)
# Button(root, image=photo, borderwidth=0, command=s).pack(side=TOP, anchor=E) # TODO Finish settings
root.title("Wrigley Engine")
image = PhotoImage(file='Wrigley Engine Logo.png')
photo = image.zoom(int(1.5), int(1.5))
Label(root, image=photo).pack()
q = Entry(root, width=80)
# root.bind("<Return>", lambda event, se=q: search) # TODO Remove Search Button
# root.focus_set()
q.pack()
Button(root, text="Search",  command=lambda: search(q)).pack()
Label().pack()
Label().pack()
Label().pack()
root.mainloop()
