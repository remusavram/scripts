#-*-coding:utf-8-*-

import xml.etree.ElementTree as xml
from cStringIO import StringIO

from PySide import QtGui, QtCore
import Shiboken
import pysideuic


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


def wrapinstance(ptr, base=None):
    """
    Utility to convert a pointer to a Qt class instance
    @param ptr: long or Swig instance, Pointer to QObject in memory
    @param base: QtGui.QWidget, (Optional) Base class to wrap with
                 (Defaults to QObject, which should handle anything)
    @return: QWidget or subclass instance
    @rtype: QtGui.QWidget
    """
    if ptr is None:
        return None
    ptr = long(ptr)  # Ensure type
    if 'shiboken' in globals():
        if base is None:
            qObj = shiboken.wrapInstance(long(ptr), QtCore.QObject)
            metaObj = qObj.metaObject()
            cls = metaObj.className()
            superCls = metaObj.superClass().className()
            if hasattr(QtGui, cls):
                base = getattr(QtGui, cls)
            elif hasattr(QtGui, superCls):
                base = getattr(QtGui, superCls)
            else:
                base = QtGui.QWidget
            # END if
        # END if
        return shiboken.wrapInstance(long(ptr), base)
    elif 'sip' in globals():
        base = QtCore.QObject
        return sip.wrapinstance(long(ptr), base)
    else:
        return None
# end def wrapinstance


def get_cpp_pointer(widget):
    """Convert cpp pointer of"""
    return long(shiboken.getCppPointer(widget)[0])
# END def get_cpp_pointer
