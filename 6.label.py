from tkinter import *

root = Tk()
root.geometry("500x500")

label = Label(root, text="Abhiram B S")
# updating label
# label['text'] = "Abhiram B S Javalli Tudoor Thirthahalli Shimoga karnataka"

# updating label using config method

# label.config(text="Abhiram B S Javalli Tudoor Thirthahalli Shimoga Karnataka")


# updating font
# label['font'] = "Times 15"

# updating font using config method
# label.config(font="Times 15")

# updating foreground
# label['fg'] = 'blue'

#updating foreground using config method
# label.config(fg='yellow')

# updating background
# label['bg'] = 'blue'

# updating background using config method
# label.config(bg='red')

label.config(text="Abhiram B S Javalli Tudoor Thirthahalli Shimoga Karnataka")

# udpate wraplength
# label['wraplength'] = '150'

# update wraplenght using config method

label.config(wraplength='150')


# update justify content -> RIGHT, LEFT and CENTER(defualt)

# label['justify'] = RIGHT
# label['justify'] = LEFT
# label['justify'] = CENTER

# update justify content using config method

label.config(justify=RIGHT)

label.pack()

root.mainloop()