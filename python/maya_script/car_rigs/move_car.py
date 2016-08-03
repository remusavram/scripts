'''

Created on Apr 22, 2013

@author: Remus


#######################
#       Theme 2       #
#######################

 
 Using "Audi R8.ma" scene, create a script that move a car.

 Deadline 29.04.2013

########################   
# Feedback: 29.04.2013 #
########################

 - Use only one procedure for wheel and chassis                       done
 - During the movement, move up and down the car (nigger style)       done
 - Create "Cancel" button for dialog box                              done
 - Open the doors                                                     new script for this
 - Use getAttr to save the distance of diameter Circle                diameterCircle is a list; it should be a float number
'''


import maya.cmds as mc

PI = 3.14

# use getAttr to save the distance of diameter Circle
diameterCircle = mc.getAttr("diameterCircleObject.distance")
circleLength = PI * diameterCircle

# Set up playback
startFrame = mc.playbackOptions(query=True, minTime=True)
endFrame = mc.playbackOptions(query=True, maxTime=True)
mc.currentTime(startFrame, edit=True, update=False)


def moveRotate(object, coverDistance, rotation):
    '''This procedure moves the care like this:
    First it setup the first keyframe, than check if the object is a wheel.
    If is not a wheel, than it moves the object.
    If is a wheel it moves and rotates the object.'''
    currentFrame = startFrame
    mc.currentTime(currentFrame, edit=True, update=False)
    # Setup first Keyframe
    mc.setKeyframe(object)
    '''    
    # Check if the object is a circle
    if ((object.find("Wheel") == -1) and (object.find("wheel") == -1)):
        currentFrameChassis = startFrame
        moveUpDown = 0
        while (currentFrameChassis <= endFrame):
            mc.move(0, moveUpDown, coverDistance/endFrame, object, r=True)
            checkCurrentFrameChassis = int(currentFrameChassis/10 % 2)

            if (checkCurrentFrameChassis == 0):
                moveUpDown = 0.1  
            else:
                moveUpDown = -0.1
            currentFrameChassis += 1
            mc.currentTime(currentFrameChassis, edit=True, update=False)
            # Create a new Keyframe
            mc.setKeyframe(object)
    
    else:
        currentFrameWheel = startFrame
        while (currentFrameWheel <= endFrame):
            previousRotation = mc.getAttr(object + ".rotateX")
            mc.rotate((rotation/endFrame)+previousRotation, 0, 0, object, os=True)
            mc.move(0, 0, coverDistance/endFrame, object, r=True)
            currentFrameWheel += 1
            mc.currentTime(currentFrameWheel, edit=True, update=False)
            # Create a new Keyframe
            mc.setKeyframe(object)
    '''    
     
     
            
    currentFrameCar = startFrame
    moveUpDown = 0            
    while (currentFrameCar <= endFrame):
        if ((object.find("Wheel") == -1) and (object.find("wheel") == -1)):
            mc.move(0, moveUpDown, coverDistance/endFrame, object, r=True)
            checkcurrentFrameCar = int(currentFrameCar/50 % 2)

            if (checkcurrentFrameCar == 0):
                moveUpDown = 0.02
            else:
                moveUpDown = -0.02
            currentFrameCar += 1

        else:
            previousRotation = mc.getAttr(object + ".rotateX")
            mc.rotate((rotation/endFrame)+previousRotation, 0, 0, object, os=True)
            mc.move(0, 0, coverDistance/endFrame, object, r=True)
            currentFrameCar += 1
        mc.currentTime(currentFrameCar, edit=True, update=False)
        # Create a new Keyframe
        mc.setKeyframe(object)
  




# Create a dialog window for introducing the distance
longDistance = mc.promptDialog(message="Please input the distance", messageAlign="center", button=['Cancel', 'OK'],
                             cancelButton="Cancel", defaultButton='OK', scrollableField=True, text="0", title="Distance")
# Check if a value has been insert in the Dialog box
# and use it for moving the car
if longDistance == "OK":
    coverDistance = mc.promptDialog(query=True, text=True)
    if (coverDistance != "Null"):
        coverDistance = int(coverDistance)        
        rotationWheel = (360 * coverDistance/circleLength)
        moveRotate("Wheel_1", coverDistance, rotationWheel)
        moveRotate("Wheel_2", coverDistance, rotationWheel)
        moveRotate("Wheel_3", coverDistance, rotationWheel)
        moveRotate("Wheel_4", coverDistance, rotationWheel)
        moveRotate("Chassis", coverDistance, rotationWheel)
        # Scroll frame by frame
        currentFrame = startFrame
        while (currentFrame <= endFrame):
            mc.currentTime(currentFrame)
            currentFrame += 1
