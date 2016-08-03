'''
Created on Mar 20, 2014

@author: Remus
'''



import maya.cmds as mc

lights = cmds.ls(lights=True)

def gainLights(lightsList, gain):

    for light in lights:
        cmds.select(light, r=True)
        intens = cmds.getAttr(".intensity")
        newIntensity = intens * gain
        mc.setAttr(".intensity", newIntensity)
        print light, "Old: ", intens, "New: ", newIntensity