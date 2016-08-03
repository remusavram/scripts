import maya.cmds as mc

def getSGfromShader(shader=None):
    if shader:
        if mc.objExists(shader):
            sgq = mc.listConnections(shader, d=True, et=True, t='shadingEngine')
            if sgq:
                return sgq[0]
        
    return None


def assignObjectListToShader(objList=None, shader=None):
    """
    Assign the shader to the object list
    arguments:
        objList: list of objects or faces
    """
    # assign selection to the shader
    shaderSG = getSGfromShader(shader)
    if objList:
        if shaderSG:
            mc.sets(objList, e=True, forceElement=shaderSG)
        else:
            print 'The provided shader didn\'t returned a shaderSG'
    else:
        print 'Please select one or more objects'


def assignSelectionToShader(shader=None):
    sel = mc.ls(sl=True, l=True)
    if sel:
        assignObjectListToShader(sel, shader)


assignSelectionToShader('lambert2')