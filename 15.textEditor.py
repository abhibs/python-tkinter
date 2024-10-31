from tkinter import *

root = Tk()

root.geometry("550x550")


def getValue():
    result = texteditor.get(1.0, END)
    print(result)

texteditor = Text(root, width=30, height=10, font=(("Times"), 15), wrap='word')
texteditor.grid(row=0, column=0, padx=40, pady=20)
texteditor.insert(INSERT, "Abhiram B S Javalli")
texteditor.config(state='disabled')
texteditor.config(state='normal')
button = Button(root, text="Save", width=10, height=1, command=getValue)
button.grid(row=3, column=0)

root.mainloop()