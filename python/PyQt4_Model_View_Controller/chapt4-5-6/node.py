#!/usr/bin/python

'''
@package   node
@brief     Used for children-parent relationship.
@details
@author    Remus Avram
@date      2014.12
'''



class Node(object):
    
    def __init__(self, name, parent=None):
        self._name = name
        self._children = []
        self._parent = parent
        
        if parent is not None:
            parent.addChild(self)
    # END def __init__
    
    def typeInfo(self):
        return "NODE"
    # END def typeInfo
    
    def addChild(self, child):
        self._children.append(child)
        child._parent = self
    # END def addChild
    
    def insertChild(self, position, child):
        if position < 0 or position > len(self._children):
            return False
        self._children.insert(position, child)
        child._parent = self
        return True
    # END def insertChild
    
    def removeChild(self, position):
        if position < 0 or position > len(self._children):
            return False
        child = self._children.pop(position)
        child._parent = None
        return True
    # END def removeChild
    
    def name(self):
        return self._name
    # END def name
    
    def setName(self, name):
        self._name = name
    
    def child(self, row):
        return self._children[row]
    # END def child
    
    def childCount(self):
        return len(self._children)
    # END def childCount
    
    def parent(self):
        return self._parent
    # END def parent
    
    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)
    # END def row
    
    def log(self, tabLevel=-1):
        output = ""
        tabLevel += 1
        for i in range(tabLevel):
            output += "\t"
        output += "|-----------" + self._name + "\n"
        for child in self._children:
            output += child.log(tabLevel)
        tabLevel -= 1
        output += "\n"
        return output
    # END def log
    
    def __repr__(self):
        return self.log()
    # END def __repr__
# END class Node


class TransformNode(Node):
    
    def __init__(self, name, parent=None):
        super(TransformNode, self).__init__(name, parent)
        
        self._x = 0
        self._y = 0
        self._z = 0
    # END def __init__
    
    def typeInfo(self):
        return "TRANSFORM"
    # END def typeInfo
    
    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def z(self):
        return self._z
    
    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y
    
    def setZ(self, z):
        self._z = z
# END class TransformNode


class CameraNode(Node):
    
    def __init__(self, name, parent=None):
        super(CameraNode, self).__init__(name, parent)
        
        self._motionBlur = True
        self._shakeIntensity = 50.0
    # END def __init__
    
    def typeInfo(self):
        return "CAMERA"
    # END def typeInfo
    
    def motionBlur(self):
        return self._motionBlur
    
    def shakeIntensity(self):
        return self._shakeIntensity
    
    def setMotionBlur(self, blur):
        self._motionBlur = blur
    
    def setShakeIntensity(self, intensity):
        self._shakeIntensity = intensity
# END class CameraNode


class LightNode(Node):
    
    def __init__(self, name, parent=None):
        super(LightNode, self).__init__(name, parent)
                
        self._lightIntensity = 1.0
        self._nearRange      = 40.0
        self._farRange       = 80.0
        self._castShadows    = True
    # END def __init__
    
    def typeInfo(self):
        return "LIGHT"
    # END def typeInfo
    
    def lightIntensity(self):
        return self._lightIntensity
    
    def nearRange(self):
        return self._nearRange
    
    def farRange(self):
        return self._farRange
    
    def castShadows(self):
        return self._castShadows
    
    def setLightIntensity(self, intensity):
        self._lightIntensity = intensity
        
    def setNearRange(self, range):
        self._nearRange = range
        
    def setFarRange(self, range):
        self._farRange = range
    
    def setCastShadows(self, cast):
        self._castShadows = cast
# END class LightNode


def main():
    '''Only for tests'''
    nodeObject = Node("hips")
# END def main

if __name__ == '__main__': main()
