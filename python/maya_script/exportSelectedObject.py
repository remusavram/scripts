""" 
#    @path        D:\Programare\Python\Another scripts
#    @file        exportSelectedObject.py
#    @brief       This script exports selected objects in another scene.


#    @author      remus_avram
#    @date        01.2014
"""



import maya.cmds as cmds



def final():
    winName="exportObjects"
    
    if ( cmds.window(winName,exists=True)):
        cmds.deleteUI(winName)
    
    cmds.window(winName,title='Export Selected Objects to New Scene',w=200,h=50)
    cmds.columnLayout(adj=True)
    cmds.textFieldButtonGrp('tfb',bl='Export',text='select objects and export to new scene',ed=False,bc='export()')
    
    cmds.showWindow(winName)

def export():
    sel=cmds.ls(sl=True)
    # check if it is something selected otherwise it gets an error;
    # a message can be printed if case nothing is selected
    if sel:
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        filename = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2)
        cmds.file( filename[0], type='mayaAscii', exportAsReference=True )
        
        
        #cmds.file( rename=filename[0] )
        #cmds.file( save=True, type='mayaAscii' )


final()