"""
#    @path
#    @file
#    @brief    Hello CreativeCrash community, I've run into a bit of a problem in Python which i've
               been strugging for days (because i'm a newb who still has much to learn).  I'm trying
               to make a UI that can list the meshes and shaders in a scene and connect the two
               selected from that list by using a button. The UI "LOOKS" functional but the connect
               button isn't doing what i want it to do T_T.

#    @author    Aaron_Williams
#    @date      15.12.2013
"""



import maya.cmds as cmds



def GUI():
    winName="myWindow"
 
    if ( cmds.window(winName,exists=True)):
        cmds.deleteUI(winName)
 
    cmds.window(winName,title='mesh/shader connector',w=200,h=500)
    cmds.window(winName,q=True,wh=True)
 
    cmds.rowLayout("obj,shd",nc=2,w=200,h=200)
    cmds.columnLayout( adj=True, columnAttach=('left', 5), rowSpacing=10, columnWidth=250 )
    cmds.textScrollList('obj')
    cmds.textScrollList('shd')  
    cmds.textFieldButtonGrp('obj',bl='Import Object', text='Select Object',ed=False, bc='selMultipleObjects()')
    cmds.textFieldButtonGrp('shd',bl='Refresh Shaders', text='Refresh Shaders',ed=False, bc='shadeGrps()')
    cmds.button(c='Connect()',l='Connect')
    cmds.showWindow()
 
GUI()
 
def selObjName():
    sel=cmds.ls(sl=True)[0]
    cmds.textFieldButtonGrp('obj',e=True,text=sel)
 
 
def selMultipleObjects():
    sel=cmds.ls(sl=True)
    cmds.textScrollList('obj',e=True,ra=True)
    cmds.textScrollList('obj',e=True,numberOfRows=len(sel)+10, allowMultiSelection=True,
            append=sel)
 
def shadeGrps():            
    Shader=cmds.ls(mat=True)
    cmds.textScrollList('shd',e=True,ra=True)
    cmds.textScrollList('shd',e=True,numberOfRows=10,append=Shader)
 
def Connect():
    cmds.shadingConnection( 'shd', e=True, cs=0 )
    cmds.shadingConnection( 'obj', q=True, cs=True )
