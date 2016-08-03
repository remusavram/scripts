'''
Created on May 18, 2013

@author: Remus


#######################
#      Theme 3        #
#######################

This script import in a window all the shaders from hypershade and assign a selected shader on an object.

Specifications:
 Define some shaders manually.
 Create a window with:
   - 2 columns:
       - radioButton with shaderName
       - type of shader
   - 2 buttons:
       - Color
       - Cancel
 The shaders and types of shaders are taken form Hypershade.                  
 If you check a shader, select an object and press Color button, than the specific shader will be assigned to the object.
 If you press Color button it shouldn't close the window, until you will press Cancel button. 
 Use onCommand instead for reevaluate radioColletion
'''


import maya.cmds as mc
from functools import partial

# Global variables
listMaterials = mc.ls( materials=True )
globalShaderName = listMaterials[-1]


def checkSelected(shaderName):
     global globalShaderName
     globalShaderName = shaderName


def addShaderInWindow():
    '''This function does: 
    - create radioButton for shader;
    - extract object type;'''
    # mc.checkBox(label=shader)
    radioCollection1 = mc.radioCollection()
    for material in listMaterials:
        OnCommandValue = 'checkSelected( "' + material + '")'
        mc.radioButton( material, label=material, select=True, onCommand=OnCommandValue )
        TypeShader = mc.nodeType( material )
        mc.text( label=TypeShader )    

    
def getSGfromShader( shader=None ):
    if shader:
        if mc.objExists(shader):
            sgq = mc.listConnections( shader, d=True, et=True, t='shadingEngine' )
            if sgq:
                return sgq[0]        
    return None


def assignObjectListToShader( objList=None, shader=None ):
    """
    Assign the shader to the object list
    arguments:
        objList: list of objects or faces
    """
    # assign selection to the shader
    shaderSG = getSGfromShader( shader )
    if objList:    
        if shaderSG:
            mc.sets( objList, edit=True, forceElement=shaderSG )
        else:
            print ( 'The provided shader didn\'t returned a shaderSG' )


def assignSelectionToShader( shader=None ):
    """ Assign the shader to all the selected objects. """
    selectedObject = mc.ls( sl=True, long=True )
    if selectedObject:
        assignObjectListToShader( selectedObject, shader )    
    else:
        print( 'Please select one or more objects' )
   
    
def colorButtonCommand():
    """ Assign the shader to slectin list. """
    global globalShaderName
    assignSelectionToShader(globalShaderName)
    
                                   
def closeWindow( windowName=None ):
    '''Close a window'''
    if mc.window( windowName, exists = True ):
        mc.deleteUI( windowName, window=True )  

      
def createWindow(): 
    closeWindow( 'AssignColor' )
    # Create a window
    mc.window( 'AssignColor', title = 'Assign color' )
    # Create a Layout for window
    mc.rowColumnLayout( rowSpacing=[10,10], numberOfColumns=2, columnWidth=[(1, 150), (2, 150)], parent='AssignColor' )
    mc.text( 'Shader' )
    mc.text( 'Type Shader' )
    addShaderInWindow()
    # Color + Cancel buttons
    mc.button('colorButton', label='Color', width=150, command='colorButtonCommand()' )
    mc.button('cancelButton', label='Cancel', width=150, command="closeWindow( 'AssignColor' )" )
    # Display window
    mc.showWindow( 'AssignColor' )

   
createWindow()

