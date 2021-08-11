from tkinter import *
from PIL import Image, ImageTk

def record_submit_successfully():
    print('Record Submit Successfully\nPersonal Details: ')
    record = f'Username: {user_entry.get()}\n Password: {pass_entry.get()}\n' \
             f'Age: {age_entry.get()}\nCity: {city_entry.get()}\nGender: {gender_entry.get()}\n*********************\n'
    print(f'Username: {user_entry.get()}')
    print('Age: ', age_entry.get())
    print('City: ', city_entry.get())
    print('Gender: ', gender_entry.get())
    f = open("record.txt", "a")
    f.write('Personal Details: \n')
    f.write(record)

    pass
# Python Basic GUI component initialization
root = Tk()
root.title('Afaq Dance Academy -Registration Form')
photo = PhotoImage(file ="img\\dance_logo.PNG")
root.iconphoto(False, photo)
# geometry dimension : width * hieght
root.geometry("600x580")
root.minsize(500,500)
image = Image.open('img\\dance_logo.PNG')
photo = ImageTk.PhotoImage(image)
Label(root, image=photo, bg='white').pack(anchor='ne', side=TOP, fill=X)

frame = Frame(root,padx=20, pady=35, bg='SlateBlue1',width=385, height=460)

l_username = Label(frame, text="Username  ", font='Calibri 12 bold', bg='SlateBlue1')
l_password = Label(frame, text="Password  ", font='Calibri 12 bold', bg='SlateBlue1')
l_age = Label(frame, text="Age  ", font='Calibri 12 bold', bg='SlateBlue1')
l_city = Label(frame, text="City  ", font='Calibri 12 bold', bg='SlateBlue1')
l_gender = Label(frame, text="Gender  ", font='Calibri 12 bold', bg='SlateBlue1')
l_username.grid(row=0, column=0, padx=5)
l_password.grid(row=1, column=0, padx=5, pady=15)
l_age.grid(row=2, column=0, padx=5, pady=15)
l_city.grid(row=3,  column=0, padx=5, pady=15)
l_gender.grid(row=4, column=0, padx=5, pady=15)
frame.pack(side=LEFT,expand=True, fill='both')

userVal = StringVar()
passVal = StringVar()
ageVal = IntVar()
cityVal = StringVar()
genderVal = StringVar()

user_entry = Entry(frame, textvariable=userVal , borderwidth=4)
pass_entry = Entry(frame, textvariable=passVal, show="*", borderwidth=4)
age_entry = Entry(frame, textvariable=ageVal, borderwidth=4)
city_entry = Entry(frame, textvariable=cityVal, borderwidth=4)
gender_entry = Entry(frame, textvariable=genderVal, borderwidth=4)
user_entry.grid(row=0, column=1,  padx=5)
pass_entry.grid(row=1, column=1,padx=5,pady=15)
age_entry.grid(row=2, column=1,padx=5,pady=15)
city_entry.grid(row=3, column= 1,padx=5,pady=15)
gender_entry.grid(row=4, column=1,padx=5,pady=15)


button = Button(frame, text="submit", bg='SlateBlue3', fg='white', font='Arial 10 bold', command=record_submit_successfully)
button.grid(row=5, column=0, padx=5, pady=15)
root.mainloop()  # event loop
