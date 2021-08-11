from tkinter import *
from PIL import ImageTk, Image

def resize_window(event):
    root.geometry(f'{width_entry.get()}x{height_entry.get()}')

root = Tk()
root.title('Auto Window Resizer App')
root.geometry("400x200+300+200")
root.minsize(250,130)
icon = PhotoImage(file='img\logo.png')
root.iconphoto(True, icon)

Label_1 = Label(root, text='Window Resizer App', fg='white', bg='purple3', font='Arial 15 bold')
Label_1.pack(fill='both')

frame = Frame(root, width=400, height=100, pady=10, padx=10)
width_label = Label(frame, text='Enter Width: ')
width_label.pack(side=LEFT)

width_var= StringVar()
height_var = StringVar()
width_entry = Entry(frame, textvariable=width_var)
width_entry.pack()
frame.pack()

frame1 = Frame(root, width=400, height=100, pady=5, padx=10)
height_label = Label(frame1, text='Enter Height: ')
height_label.pack(side=LEFT)
height_entry = Entry(frame1, textvariable=height_var)
height_entry.pack(padx=4)
frame1.pack()

btn = Button(text='Resize',bg='purple3', fg='white')
btn.bind('<Button-1>', resize_window)
btn.pack()

root.mainloop()
