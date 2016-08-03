# Create autoSave script

import maya.cmds as mc

intervalSeconds = 600
folderDestination = "D:/Python/My scripts/testautosave"

mc.autoSave( enable=True, interval=intervalSecunde, prompt=False, destination=1, folder=folderDestination, perform=True )