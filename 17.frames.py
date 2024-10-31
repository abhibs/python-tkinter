from tkinter import *
root = Tk()
root.title("Abhiram B S")
root.geometry("650x650+450+200")

frames = Frame(root, height=300, width=300, bg='blue')
frames.pack(fill=X)


button1 = Button(frames, text='Button 1')
button2 = Button(frames, text='Button 2')
button1.pack(side=LEFT, padx=20, pady = 50)
button2.pack(side=LEFT, padx=20, pady = 50)


root.mainloop()
