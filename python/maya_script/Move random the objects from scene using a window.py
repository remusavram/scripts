'''
Created on Apr 24, 2013

@author: Remus


 This script moves random the selected objects objects from scene using a window with:
 - a button for recalculate the position
 - 3 fields (X Y Z) for range
 - 3 fields (X Y Z) for rotate
 - 3 fields (X Y Z) for scale
'''

import maya.cmds as mc
import random
#help(random)

# Add in "selectList" the selected objects
selectList = mc.ls(selection=True)
# Create a window
disperserWindow = mc.window(title = "Dispeser", widthHeight=(256,256))
mc.columnLayout()
# Create a button inside window
mc.button(label = "Disperse Selected!", command = "disperse()")
# Create fields for distance
mc.text("Set X Y Z Range Values")
rangeField = mc.floatFieldGrp(numberOfFields=3)
# Create fildes for rotation
mc.text("Set X Y Z Rotation Values")
rotationField = mc.floatFieldGrp(numberOfFields=3)
# Create fildes for rescale
mc.text("Set X Y Z Scale Values")
scaleField = mc.floatFieldGrp(numberOfFields=3)
# Display the window
mc.showWindow(disperserWindow)

# Create a function for disperse the objects
def disperse():    
    rangeX = mc.floatFieldGrp(rangeField, query=True, value1=True)
    rangeY = mc.floatFieldGrp(rangeField, query=True, value2=True)
    rangeZ = mc.floatFieldGrp(rangeField, query=True, value2=True)
    rotationX = mc.floatFieldGrp(rotationField, query=True, value1=True)
    rotationY = mc.floatFieldGrp(rotationField, query=True, value2=True)
    rotationZ = mc.floatFieldGrp(rotationField, query=True, value3=True)
    scaleX = mc.floatFieldGrp(scaleField, query=True, value1=True)
    scaleY = mc.floatFieldGrp(scaleField, query=True, value2=True)
    scaleZ = mc.floatFieldGrp(scaleField, query=True, value3=True)
    # Use "for" loop to scroll through selectList and change the position and rotate the objects
    for obj in selectList:
        randomRangeX = random.randint(-rangeX, rangeX)
        randomRangeY = random.randint(-rangeY, rangeY)
        randomRangeZ = random.randint(-rangeZ, rangeZ)
        mc.setAttr(obj + ".translateX", randomRangeX)
        mc.setAttr(obj + ".translateY", randomRangeY)
        mc.setAttr(obj + ".translateZ", randomRangeZ)
        randomRotateX = random.randint(-rotationX, rotationX)
        randomRotateY = random.randint(-rotationY, rotationY)
        randomRotateZ = random.randint(-rotationZ, rotationZ)
        mc.setAttr(obj + ".rotateX", randomRotateX)
        mc.setAttr(obj + ".rotateY", randomRotateY)
        mc.setAttr(obj + ".rotateZ", randomRotateZ)
        randomScaleX = random.randint(-scaleX, scaleX)
        randomScaleY = random.randint(-scaleY, scaleY)
        randomScaleZ = random.randint(-scaleZ, scaleZ)
        if scaleX != 0:
            mc.setAttr(obj + ".scaleX", randomScaleX)
        if scaleY != 0:
            mc.setAttr(obj + ".scaleY", randomScaleY)
        if scaleZ != 0:    
            mc.setAttr(obj + ".scaleZ", randomScaleZ)
