from Tkinter import *

##very simple login screen (tweaks to be made) 

root = Tk()

def label(t,r,s):
    label1 = Label(root,text = t)
    label1.grid(row=r,sticky=s)

def entry(r,c):
    entry1=Entry(root)
    entry1.grid(row=r,column=c)

def button(t,r,c,s,cs):
    button1 = Button(root, text = t)
    button1.grid(row =r, column=c,sticky=s,columnspan= cs)

def checkbutton(t,cs,s):
    x = Checkbutton(root, text=t)
    x.grid(columnspan = cs,sticky =s)
    
''' OBJECTS CALLING '''

label('Name',0,E)
label('Password',1,E)
entry(0,1)
entry(1,1)
button('Login',3,1,E,2)
checkbutton('Keep Me Logged In',2,W)




root.mainloop()
    
