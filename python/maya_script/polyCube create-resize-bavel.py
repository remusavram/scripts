'''
Created on Apr 21, 2013

@author: Remus


This script create->resize->bavel a polyCube.
'''

polyCubeToBavel = mc.polyCube( w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
mc.scale(4, 4, 4, r=True)
mc.polyBevel (polyCubeToBavel, offset=0.5, offsetAsFraction=1, autoFit=1, segments=1, worldSpace=1,\
			   uvAssignment=0, fillNgons=1, mergeVertices=1, mergeVertexTolerance=0.0001,\
			   smoothingAngle=30, miteringAngle=180, angleTolerance=180, ch=1)