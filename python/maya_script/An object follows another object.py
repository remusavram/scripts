'''
Created on Apr 27, 2013

@author: Remus


 This script makes an object to follows another object which is already animated
# Use "Spheres.ma" scene for testing
'''

# import maya.cmds as mc

# Set up playback
startFrame = mc.playbackOptions(query=True, minTime=True)
endFrame = mc.playbackOptions(query=True, maxTime=True)
currentFrame = startFrame

# Initialize goal and follower
goal = "pSphere1"
follower = "pSphere2"

# Scroll frame by frame
while (currentFrame < endFrame):
#    print ("The frame is currently at %d" %currentFrame) 
#    mc.setAttr(follower + ".translate", goalTrans[0][0], goalTrans[0][1], goalTrans[0][2])
    goalTrans = mc.getAttr(goal + ".translate")
    mc.setKeyframe(follower, at="translateX", v=goalTrans[0][0]+2)
    mc.setKeyframe(follower, at="translateY", v=goalTrans[0][1]+2)
    mc.setKeyframe(follower, at="translateZ", v=goalTrans[0][2]+2)
    mc.currentTime(currentFrame)
    currentFrame += 1
	
