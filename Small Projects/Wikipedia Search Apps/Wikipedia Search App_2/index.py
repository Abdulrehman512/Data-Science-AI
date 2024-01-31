import wikipedia
from tkinter import *

def on_press():

    q = get_Q.get()
    text.insert(INSERT,wikipedia.summary(q))

root = Tk()
root.title("WIKI Search App")
question = Label(root,text="Question")
question.pack()
get_Q = Entry(root,bd=5)
get_Q.pack()
submit = Button(root,text="Search",command=on_press)
submit.pack()
text = Text(root)
text.pack()

root.mainloop