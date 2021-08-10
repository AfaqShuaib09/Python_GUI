from tkinter import *
from PIL import ImageTk, Image
import time

def type_exp(event):
    result = None
    global exp
    text = event.widget.cget('text')
    if text == "=":
        if exp.get().isdigit():
            result = exp.get()
        else:
            try:
                result = eval(exp.get())
            except Exception as e:
                print('Exception:')
                result = 'Error'
            exp.set(result)
            entry_screen.update()
    elif text == 'C':
        exp.set('')
        entry_screen.update()
    elif text =='<<':
        exp.set(exp.get()[:-1])
        entry_screen.update()
    else:
        exp.set(exp.get() + text)
        entry_screen.update()


root = Tk()
root_win_width = 650
root_win_height = 630
root.title('Afaq Calculator Inc.')
root.geometry(f'{root_win_width}x{root_win_height}')

icon = PhotoImage(file='img\\cal_logo3.PNG')
root.iconphoto(True, icon)

bg_color = 'white'
fg_color = 'SlateBlue1'

image = Image.open('img\\cal_logo3.PNG')
image = image.resize((400, 130), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
Label(root, image=photo, bg=bg_color).pack(anchor='ne', side=TOP, fill=X)

exp = StringVar()

entry_screen = Entry(root, textvariable=exp, bg=bg_color, fg=fg_color, borderwidth=3, relief=SUNKEN,
                     font='Helvetica 25 bold', justify=RIGHT)
entry_screen.pack(fill=X, padx=10, pady=3, ipady=3)

calculator_frame = Frame(root, bg='white', padx=20, pady=0)
calculator_frame.pack(fill=BOTH)
frame1_entries = ['C','<<','7','8','9']

for i in range(0, 5):
    if i % 5 != 0 and i % 5 != 1 :
        b = Button(calculator_frame, text=frame1_entries[i], padx=45, pady=30, bg='gray10', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)
    else:
        b = Button(calculator_frame, text=frame1_entries[i], padx=45, pady=30, bg='Blue', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)

calculator_frame = Frame(root, bg='white', padx=20, pady=0)
calculator_frame.pack(fill=BOTH)
frame2_entries = ['/','*','4','5','6']

for i in range(0, 5):
    if i % 5 != 0 and i % 5 != 1 :
        b = Button(calculator_frame, text=frame2_entries[i], padx=45, pady=30, bg='gray10', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)
    else:
        b = Button(calculator_frame, text=frame2_entries[i], padx=45, pady=30, bg='Blue', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)

calculator_frame = Frame(root, bg='white', padx=20, pady=0)
calculator_frame.pack(fill=BOTH)
frame3_entries = ['-','+','1','2','3']

for i in range(0, 5):
    if i % 5 != 0 and i % 5 != 1 :
        b = Button(calculator_frame, text=frame3_entries[i], padx=45, pady=30, bg='gray10', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)
    else:
        b = Button(calculator_frame, text=frame3_entries[i], padx=45, pady=30, bg='Blue', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)

calculator_frame = Frame(root, bg='white', padx=20, pady=0)
calculator_frame.pack(fill=BOTH)
frame4_entries = ['=','%','^','0','.']


for i in range(0, 5):
    if i % 5 != 0 and i % 5 != 1 :
        b = Button(calculator_frame, text=frame4_entries[i], padx=45, pady=30, bg='gray10', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)
    else:
        b = Button(calculator_frame, text=frame4_entries[i], padx=45, pady=30, bg='Blue', fg='white', font='Helvetica 15 bold')
        b.pack(side=RIGHT, padx=3, pady=4)
        b.bind('<Button-1>', type_exp)

root.mainloop()
