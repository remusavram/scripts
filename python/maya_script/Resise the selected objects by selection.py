'''
Created on Apr 21, 2013

@author: Remus


 This script resizes the selected objects by according to the order selection.
'''

#import maya.cmds as cm

listObjects = mc.ls(sl=True)
selectSize = len(listObjects)
for i in range (0, selectSize, 1):
        rescaler = (i+1)*0.2
        mc.scale(rescaler, rescaler, rescaler, listObjects[i], r=True)