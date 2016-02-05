from Tkinter import *
root = Tk()

label1 = Label(root,text = 'Name')
label2 = Label(root,text = 'Password')
entryOne = Entry(root)
entryTwo = Entry(root)

label1.grid(row=0,sticky = E)
label2.grid(row=1,sticky =E)
entryOne.grid(row=0,column = 1)
entryTwo.grid(row=1,column = 1)


x = Checkbutton(root, text='Keep me logged in')
x.grid(columnspan = 2)


root.mainloop()
