from Tkinter import *
root = Tk()

def printName():
    counter = 0
    for i in range(0,11):
        print i
        counter = counter + 1
        


def printNameNew(event):
    print 'Jordan!!'
    

button1 = Button(root, text = 'Count to 10', command =printName)
button1.grid(row = 1)
button2 = Button(root, text ='Print my name')
button2.bind('<Button-1>',printNameNew)
button2.grid(row = 2)

root.mainloop()
