'''
Created on Apr 21, 2013

@author: Remus
'''

#######################
#       Theme 1       #
#######################
#
#  create same simples polygons and change their attributes.
#
#
#
# Solution:
#
# What the scrypt does:
# - delete all selected objects
# - create new objects with different values for scale, move, rotate


import maya.cmds as mc

# Delete all selected objects
listObjects = mc.ls(sl=True)
for i in range(0, len(listObjects), 1):
    mc.delete(listObjects[i])

# Create objects with different values of scale, move, rotate
sphere = mc.polySphere (r=1, sx=20, sy=20, ax=(0,1,0), cuv=2, ch=1)
mc.scale(2, 2, 2, sphere, r=True)
mc.move(6, 0, 0, sphere, r=True)

cube = mc.polyCube (w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
mc.scale(2, 2.6, 3, cube, r=True)
mc.move(-6, 0, 0, cube, r=True)
mc.rotate(14, 4, 3.5, cube, os=True)

cylinder = mc.polyCylinder(r=1, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), rcp=0, cuv=3, ch=1)
mc.scale(2, 1, 2, cylinder, r=True)
mc.move(0, 0, -6, r=True)
mc.rotate(3, 5, 6, cylinder, r=True, os=True)

cone = mc.polyCone(r=1, h=2, sx=20, sy=1, sz=0, ax=(0, 1, 0), rcp=0, cuv=3, ch=1)
mc.scale(2, 3, 2, cone, r=True)
mc.move(6, 0, 6, cone, r=True)
mc.rotate(12, 11, 5, cone, r=True, os=True)

torus = mc.polyTorus(r=1, sr=0.5, tx=0, sx=20, sy=0, ax=(0, 1, 0), cuv=3, ch=1)
mc.scale(2, 2, 2, torus, r=True)
mc.move(-6, 0, 6, torus, r=True)
mc.rotate(1, 23, 5, torus, r=True, os=True)

prism = mc.polyPrism(w=1, ns=3, sh=1, sc=0, ax=(0, 1, 0), cuv=3, ch=1)
mc.scale(2, 2, 2, prism, r=True)
mc.move(0, 0, 6, prism, r=True)
mc.rotate(1, 4, 30, prism, r=True, os=True)

pyramid = mc.polyPyramid(w=1, ns=4, sh=0, sc=0, ax=(0, 1, 0), cuv=3, ch=1)
mc.scale(4, 5, 4, pyramid, r=True)
mc.move(6, 0, -6, pyramid, r=True)

pipe = mc.polyPipe(r=1, h=3, t=0.5, sa=20, sh=1, sc=0, ax=(0, 1, 0), cuv=3, rcp=0, ch=1)
mc.scale(2, 2, 2, pipe, r=True)
mc.move(-6, 0, -6, pipe, r=True)
mc.rotate(14, 32, 30, pipe, r=True, os=True)

helix = mc.polyHelix(c=3, h=2, w=2, r=0.4, sa=8, sco=50, sc=0, d=1, ax=(0, 1, 0), cuv=3, rcp=0, ch=1)
mc.scale(2, 2, 2, helix, r=True)
mc.move(0, 0, 0, helix, r=True)
mc.rotate(14, 32, 90, helix, r=True, os=True)

# Deselect all 
mc.select(clear=True)