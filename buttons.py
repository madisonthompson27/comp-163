#goal of this program is to make the buttons flip flop enabled states, so that when the on button is clicked the off button is disabled
#and the on button becomes the disabled off button

from tkinter import *

#root functions
root = Tk()
root.title("Flip Flop")

#defining lambda function
def toggle(num):
    if num == 1:
        btnOn["text"] = "Off"
        btnOff["text"] = "On"
        btnOn["state"] = DISABLED
        btnOff["state"] = NORMAL
    
    else:
        btnOn["text"] = "On"
        btnOff["text"] = "Off"
        btnOn["state"] = NORMAL
        btnOff["state"] = DISABLED

#defining count clicks
def countClicks():
    clicks = 0
    clicks = clicks + 1
    print(f'Clicks: {clicks}')

#instantiating the buttons
btnOn = Button(root, text="Button on", padx=40, pady=10, command=lambda: toggle(1))
btnOff = Button(root, text="Button off", state=DISABLED, padx=40, pady=10, command=lambda: toggle(2))
lblClicks = Label(root, command=countClicks())

#packing
btnOn.pack()
btnOff.pack()
lblClicks.pack()

root.mainloop()