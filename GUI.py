from Tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

def button(buttonText, fgcolour,bgcolour):
    button1 = Button(topFrame, text= buttonText, fg = fgcolour, bg = bgcolour)
    button1.pack(side = LEFT)
    

def label(textOne):
    label1 = Label(topFrame, text = textOne)
    label1.pack()

    


button('Hello', 'white','black')
button('World' ,'blue', 'orange')
button('!', 'black', 'cyan')
label('dhujdhjsdj') 
root = mainloop()
