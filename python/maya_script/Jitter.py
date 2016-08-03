#Import Desired Libraries Here
import maya.OpenMaya as om
import maya.OpenMayaMPx as omMPx
import random

#Set name and id
nodeName = "jitter"
nodeId = om.MTypeId(0x101112)

# Jitter Node - uses MPxNode as a base
class jitterNode(omMPx.MPxNode):
    # input and output variables
    INPUT = om.MObject()
    OUTPUT = om.MObject()

    def __init__(self):
        omMPx.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        if (plug == jitterNode.OUTPUT):
            dataHandle = dataBlock.inputValue(jitterNode.INPUT)
            inFloat = dataHandle.asFloat()
            result = random.uniform(-1,1) + inFloat
            outputHandle = dataBlock.outputValue(jitterNode.OUTPUT)
            outputHandle.setFloat(result)
            dataBlock.setClean(plug)
                

def nodeCreator():
    # Create Jitter Node
    return omMPx.asMPxPtr( jitterNode() )

def nodeInit():
    # Init me
    numAttr = om.MFnNumericAttribute()
    jitterNode.INPUT = numAttr.create("input", "in", om.MFnNumericData.kFloat, 0.0)
    numAttr.setStorable(1)

    numAttr = om.MFnNumericAttribute()
    jitterNode.OUTPUT = numAttr.create("output" , "out", om.MFnNumericData.kFloat, 0.0)
    numAttr.setStorable(1)
    numAttr.setWritable(1)

    jitterNode.addAttribute(jitterNode.INPUT)
    jitterNode.addAttribute(jitterNode.OUTPUT)
    jitterNode.attributeAffects(jitterNode.INPUT, jitterNode.OUTPUT)

# This is used for loading plugins
def initializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(nodeName, nodeId, nodeCreator, nodeInit)
    except:
        sys.stderr.write("Error loading")
        raise

# This is used for removing plugins
def uninitializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeId )
    except:
        sys.stderr.write("Error removing")
        raise
