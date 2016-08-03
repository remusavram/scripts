'''
Created on May 5, 2013

@author: Remus


 The script create swords which follow another sword.

 Use Expression Editor (Windows -> Animation Editors -> Expression Editor)
 Use scene "Swords.ma".
'''

import maya.cmds as mc


def lag(frame, goal, follower, lagAmount):
	'''
	This function move and rotate the swordFollower by swordGoal
	This function is used in Expression Editor called "swordExpresion":
		python ("lag(" + frame + ", 'swordGoal', 'swordFollower1', 0.3)");
	" + frame + " we are using "+" for concatenation because "frame" is a MEL command
	'''
	goalTrans = mc.getAttr(goal + ".translate", t=frame-lagAmount)
	goalRot = mc.getAttr(goal + ".rotate", t=frame-lagAmount)
	mc.setAttr(follower + ".translate", goalTrans[0][0], goalTrans[0][1], goalTrans[0][2])
	mc.setAttr(follower + ".rotate", goalRot[0][0], goalRot[0][1], goalRot[0][2])
