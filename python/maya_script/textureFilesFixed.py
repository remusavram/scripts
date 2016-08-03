'''
Created on Mar 20, 2014

@author: Remus
'''



import maya.cmds as mc
import os

fileNodes = mc.ls(type='file')
pathTextureFiles = "D:\Programare\Python\Tutorials Scripts\CMIVFX - Python Introduction Vol 01\ProjectFile\\textures\\"

def textureFile(fileNodes, pathTextureFiles):
    """ This function fixes the path of textures. """
    
    for f in fileNodes:
        attrib = "%s.fileTextureName" %f
        fullname = mc.getAttr(attrib)
        nameFile = os.path.split(fullname)[-1]
        newNameFile = os.path.join(pathTextureFiles, nameFile)
        mc.setAttr(".fileTextureName", newNameFile, type="string")
    
textureFile(fileNodes, pathTextureFiles)