'''
Created on Mar 20, 2014

@author: Remus
'''



import maya.cmds as mc

height = 0
degrees = 0

for i in range(200):
    spiralSphere = "spiralSphere_" + str(1)
    partsSpiral = mc.sphere(name=spiralSphere, pivot=(3, height, 0))
    transform = partsSpiral[0]
    
    myAttr = transform + ".rotateY"
    mc.setAttr(myAttr, degrees)
    
    height += 1
    degrees += 10

