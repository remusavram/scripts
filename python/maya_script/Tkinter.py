import maya.standalone
maya.standalone.initialize()

import maya.cmds as mc

import os

import Tkinter as tk

# create a window
app = tk.Tk()

def makeCube():
    print "polyCube was added"
    mc.polyCube()
    
def saveFile():
    print "file has been saved"
    mc.file(rename="C:/cubetemp.ma")
    mc.file(save=True)
    
# Create a button
btnCube = tk.Button(app, text="Make a Cube!", command= makeCube)
# Make the button visible
btnCube.pack()

btnSave = tk.Button(app, text="Sabe File!", command=saveFile)
btnSave.pack()

# close the windows completely
app.protocol("WM_DELETE_WINDOW", app.quit)
# show the window
app.mainloop()
app.destroy()
os._exit(0)
