from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Abhiram B S")
root.geometry("450x450+650+350")


progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progress.pack(pady=20)
# progress.config(mode='indeterminate')
progress.config(mode='determinate', maximum=50.0, value=10.0)
progress.start()
progress.stop()


value = DoubleVar()
progress.config(variable=value)

scale = ttk.Scale(root, orient=HORIZONTAL,var=value, length=200, from_=0.0, to=50.0)
scale.pack()

root.mainloop()