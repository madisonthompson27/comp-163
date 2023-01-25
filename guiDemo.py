#implementation of TK can be pulled from pylibrary and should come standard in python3 and above (import as mod)

# * is a wildcard that imports everything, not SOP
from tkinter import *

#widgets are created and must be instantiated (they are objects) and then placed

#creating a GUI is moving to event-drived program, instead of object-oriented programming

#instantiating root 
root = Tk()

#defining buttonClick
def buttonClick():
    lblClicked = Label(root, entData.get())
    lblClicked.pack()

#creating widget
lblData = Label(root, text="Aggie Pride")
lblWorld = Label(root, text="World Wide")
lblSpace = Label(root, text=" ")
btnClickMe = Button(root, text="Click Me!", padx=10, pady=15, command=buttonClick)


#entries
entData = Entry(root)

#place widget
#lblData.grid(row=0, column=1)
#lblWorld.grid(row=1, column=11)
#lblSpace.grid(row=2, column=2)
entData.pack()
btnClickMe.pack()


root.mainloop()