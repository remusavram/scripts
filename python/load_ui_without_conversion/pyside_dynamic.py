#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Copyright (c) 2011 Sebastian Wiesner <lunaryorn@gmail.com>

"""
@brief         How to load a user interface dynamically with PySide.
@author        Sebastian Wiesner
@email         lunaryorn@gmail.com
@date          2014.11
"""


from __future__ import (print_function, division, unicode_literals,
                        absolute_import)

import os
import sys

from PySide.QtCore import Slot, QMetaObject
from PySide.QtUiTools import QUiLoader
from PySide.QtGui import QApplication, QMainWindow, QMessageBox


#uiFile = os.path.join(os.path.dirname(__file__), './ui/testUI.ui')
uiFile = './ui/testUI.ui'

class UiLoader(QUiLoader):
    """
    Subclass :class:`~PySide.QtUiTools.QUiLoader` to create the user interface
    in a base instance.

    Unlike :class:`~PySide.QtUiTools.QUiLoader` itself this class does not
    create a new instance of the top-level widget, but creates the user
    interface in an existing instance of the top-level class.

    This mimics the behaviour of :func:`PyQt4.uic.loadUi`.
    """

    def __init__(self, baseinstance):
        """
        Create a loader for the given ``baseinstance``.

        The user interface is created in ``baseinstance``, which must be an
        instance of the top-level class in the user interface to load, or a
        subclass thereof.

        ``parent`` is the parent object of this loader.
        """
        QUiLoader.__init__(self, baseinstance)
        self.baseinstance = baseinstance
    # END def __init__

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.baseinstance:
            # supposed to create the top-level widget, return the base instance
            # instead
            return self.baseinstance
        else:
            # create a new widget for child widgets
            widget = QUiLoader.createWidget(self, class_name, parent, name)
            if self.baseinstance:
                # set an attribute for the new child widget on the base
                # instance, just like PyQt4.uic.loadUi does.
                setattr(self.baseinstance, name, widget)
            return widget
    # END def createWidget
# END class UiLoader


def loadUi(uifile, baseinstance=None):
    """
    Dynamically load a user interface from the given ``uifile``.

    ``uifile`` is a string containing a file name of the UI file to load.

    If ``baseinstance`` is ``None``, the a new instance of the top-level widget
    will be created.  Otherwise, the user interface is created within the given
    ``baseinstance``.  In this case ``baseinstance`` must be an instance of the
    top-level widget class in the UI file to load, or a subclass thereof.  In
    other words, if you've created a ``QMainWindow`` interface in the designer,
    ``baseinstance`` must be a ``QMainWindow`` or a subclass thereof, too.  You
    cannot load a ``QMainWindow`` UI file with a plain
    :class:`~PySide.QtGui.QWidget` as ``baseinstance``.

    :method:`~PySide.QtCore.QMetaObject.connectSlotsByName()` is called on the
    created user interface, so you can implemented your slots according to its
    conventions in your widget class.

    Return ``baseinstance``, if ``baseinstance`` is not ``None``.  Otherwise
    return the newly created instance of the user interface.
    """
    loader = UiLoader(baseinstance)
    widget = loader.load(uifile)
    QMetaObject.connectSlotsByName(widget)
    return widget
# END def loadUi


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi(uiFile, self)
        
        #self.pushButtonOK.clicked.connect(self.OKmethod)
    # END def __init__
        
    def OKmethod(self):
        print ("You pressed OK button!")
    # END def OKmethod
# END class MainWindow
        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
# END def main


if __name__ == '__main__': main()
