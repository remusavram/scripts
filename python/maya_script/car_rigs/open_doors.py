'''

Created on Apr 22, 2013

@author: Remus


#######################
#      Theme 2.2      #
#######################

 
 Using "Audi R8_open_doors.ma" scene, create a script that open Audi R8 doors.

'''


import maya.cmds as mc


# Set up playback
startFrame = mc.playbackOptions(query=True, minTime=True)
endFrame = mc.playbackOptions(query=True, maxTime=True)
mc.currentTime(startFrame, edit=True, update=False)


def openDoor(object, sign):
    '''This procedure opens a door.'''
    currentFrame = startFrame
   
    # Setup first Keyframe
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
    
    # First move and rotate
    mc.move(sign*0.2, 0, 0, object, r=True)
    mc.rotate(0, sign* (-19), 0, object, r=True, os=True)
    # Setup second Keyframe
    currentFrame = currentFrame + 10
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
        
    # Second move and rotate
    mc.rotate(3.4, 0, 0, object, r=True, os=True)
    mc.rotate(0, sign*(-6.2), 0, object, r=True, os=True)
    mc.rotate(0, 0, sign*(-2.8), object, r=True, os=True)
    # Setup third Keyframe
    currentFrame = currentFrame + 7
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
    
    # Third move and rotate
    mc.rotate(25, 0, 0, object, r=True, os=True)
    # Setup fourth Keyframe
    currentFrame = currentFrame + 7
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
    
    # Fourth move and rotate
    mc.rotate(3, 0, 0, object, r=True, os=True)
    mc.rotate(0, sign*3, 0, object, r=True, os=True)
    # Setup fifth Keyframe
    currentFrame = currentFrame + 4
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
    
    # 5 move and rotate
    mc.rotate(20, 0, 0, object, r=True, os=True)
    mc.rotate(0, sign*(-1.5), 0, object, r=True, os=True)
    mc.rotate(0, 0, sign*(-4.5), object, r=True, os=True)
    # Setup 6 Keyframe
    currentFrame = currentFrame + 8
    mc.currentTime(currentFrame, edit=True, update=False)    
    mc.setKeyframe(object)
    
    

openDoor('left_door', sign=1)
openDoor('right_door', sign=-1)

currentFrame = startFrame
while (currentFrame <= endFrame):
    mc.currentTime(currentFrame)
    currentFrame += 1
    
    
