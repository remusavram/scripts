'''
Created on Apr 21, 2013

@author: Remus


 This script creates a screw nut with teeth.
 Using a dialog box, let the user to introduce the number of teeth.
'''

# import maya.cmds as mc

# Create a dialog window
pdStatus = mc.promptDialog(message="Please input number of teeth", button="OK")
# Check if "OK" button has been pressing and use "numTeeth" value to store the number entered
# and convert the text in a number
if pdStatus == "OK":
    numTeeth = mc.promptDialog(query=True, text=True)
    numTeeth = int(numTeeth)
    # Create a polyPipe using "gear" variable
    gear = mc.polyPipe(subdivisionsAxis=numTeeth*2, height=0.5)
    # Set the value of intSA to be the pipe's subdivision axis
    intSA = mc.getAttr(gear[1]+".subdivisionsAxis")
    # Use formula to derive the start and end outer face
    intStartFace = intSA * 2
    intEndFace = (intSA * 3) - 1
    # Deselect all
    mc.select(clear=True)
    # Use for loop to select every other face
    for i in range (intStartFace, intEndFace+1, 2):
        mc.select(gear[0]+".f[%d]" %i, tgl=True)
    # Extrude selected faces    
    mc.polyExtrudeFacet(ltz=0.5)
    mc.polySmooth(gear[0], continuity=0.5)
