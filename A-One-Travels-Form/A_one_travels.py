from tkinter import *
from PIL import Image, ImageTk

def getval():
    print("Record Submit Successfully")
    record = f'Name: {name_entry.get()}\n Phone: {phone_entry.get()}\n' \
             f'Gender : {gender_entry.get()}\nEmergency Contact: {emergency_entry.get()}\n' \
             f'PaymentMode: {payment_mode_entry.get()}\nPre-FoodBooking: {str(food_service_val.get())}\n*********************\n'
    f = open("travel_record.txt", "a")
    f.write('Personal Details: \n')
    f.write(record)


root = Tk()
root.title('A-One Travels Booking Form')
root.geometry('500x400+300+100')
root.maxsize(500,500)
photo = PhotoImage(file ="img\\Travle.png")
root.iconphoto(False, photo)
color_var = 'cornflower blue'

image = Image.open('img\\Travle.png')
photo = ImageTk.PhotoImage(image)
Label(root, image=photo, bg='white').pack(anchor='ne', side=TOP, fill=X)
#Label(root, text='Welcome to the A-one Travels', font="comicsansns 13 bold").pack()

frame = Frame(root,bg='cornflower blue', pady=15)
name = Label(frame, text='Name',bg=color_var).grid(row=1, column=0, pady=3)
phone = Label(frame, text='Phone', bg=color_var).grid(row=2, column=0, pady=3)
gender = Label(frame, text='Gender',bg=color_var).grid(row=3, column=0, pady=3)
emergency_contact = Label(frame, text='Emergency Contact', bg=color_var).grid(row=4, column=0, pady=3)
payment_mode = Label(frame, text='Payment Mode', bg=color_var).grid(row=5, column=0, pady=3)

name_val = StringVar()
phone_val = StringVar()
gender_val = StringVar()
emergency_con_val = StringVar()
payment_mode_val = StringVar()
food_service_val = IntVar()

name_entry = Entry(frame, textvariable=name_val)
name_entry.grid(row=1, column=1, padx=2)
phone_entry = Entry(frame, textvariable=phone_val)
phone_entry.grid(row=2, column=1, padx=2)
gender_entry = Entry(frame, textvariable=gender_val)
gender_entry.grid(row=3, column=1, padx=2)
emergency_entry = Entry(frame, textvariable=emergency_con_val)
emergency_entry.grid(row=4, column=1, padx=2)
payment_mode_entry = Entry(frame, textvariable=payment_mode_val)
payment_mode_entry.grid(row=5, column=1, padx=2)
food_service = Checkbutton(frame, text="Want to prebook the meal?", variable=food_service_val,bg=color_var, onvalue=1, offvalue=0)
food_service.grid(row=6, column=1)

submit_btn = Button(frame, text="Submit to A-one Travels",bg=color_var, command=getval).grid(row=7, column=0, padx=15)
frame.pack(side=LEFT, expand=True, fill='both')
root.mainloop()
