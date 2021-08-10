from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
import time
from tkinter.messagebox import showinfo
import os


def newFile():
    global file
    root.title("Untitled - Afaq Note++")
    file = None
    TextArea.delete(1.0, END)


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def quitApp():
    quit()


def cut():
    TextArea.event_generate(("<<Cut>>"))
    pass


def copy():
    TextArea.event_generate(("<<Copy>>"))
    pass


def paste():
    TextArea.event_generate(("<<Paste>>"))
    pass


def about():
    showinfo("Code++", f'Code++ Developed by Muhammad Afaq Shuaib \U0001F600')


if __name__ == '__main__':
    root = Tk()
    root_win_height = 450
    root_win_width = 600
    root.title('Untitled -Afaq Note++')
    root.geometry(f'{root_win_width}x{root_win_height}')
    icon = PhotoImage(file='img\\note++logo2.PNG')
    root.iconphoto(True, icon)

    MenuBar = Menu(root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    # To Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit Menu Start
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Note++", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    root.config(menu=MenuBar)

    image = Image.open('img\\note++logo.PNG')
    image = image.resize((300, 80), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    Label(root, image=photo, bg='white').pack(anchor='ne', side=TOP, fill=X)

    TextArea = Text(root, font="Calibiri 10")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
