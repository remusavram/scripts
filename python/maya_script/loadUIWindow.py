"""
@brief         This script loads an UI file in Maya without converting it.
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.08
"""

import xml.etree.ElementTree as xml
from cStringIO import StringIO

from PySide import QtGui, QtCore
import Shiboken
import pysideuic
from maya import OpenMayaUI


def loadUiType(ui_file):
    """
    Pyside lacks the "loadUiType" command, so we have to convert
    the ui file to py code in-memory first and then execute it in
    a special frame to retrieve the form_class.
    """
    parsed = xml.parse(ui_file)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text
    
    with open(ui_file, 'r') as f:
        o = StringIO()
        frame = {}
    
        pysideuic.compileUi(f, o, indent=0)
        
        pyc = compile(o.getvalue(), '<string>', 'exec')
        
        exec pyc in frame
        
        # Fetch the base_class and form_class based on their type
        # in the xml from designer
        form_class = frame['Ui_%s' % form_class]
        base_class = eval('QtGui.%s' % widget_class)
        
    return form_class, base_class    
    # end def loadUiType


uiFile =  'C:/testUI.ui'

base_class, form_class = loadUiType(uiFile)
print base_class, form_class

class Manager(base_class, form_class):
    """The super class for the Asset Manager, the Scene Manager and the
    Constructor Manager.
    """
    
    def __init__(self, title='Manager'):
        """Initializes the manager.
        @param title: the window title
        @type title: String
        
        """
        super(Manager, self).__init__()
        self.setupUi(self)
    


base_class, form_class = loadUiType(uiFile)
managerObject = Manager()

managerObject.show()