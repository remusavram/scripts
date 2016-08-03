#-*-coding:utf-8-*-
"""
@package tx_common.qt.utils.widgets.draggablebutton
@brief A draggable qt button

@author Sascha Kremers
@email sascha.kremers@trixter.de
@copyright 2013 TRIXTER Film GmbH
"""
__all__ = ['DraggableButton']

from PySide import QtCore, QtGui


class DraggableButton(QtGui.QToolButton):
    """Custom QToolButton that can be dragged and dropped"""
    def __init__(self):
        super(DraggableButton, self).__init__()
        self.order = None
    # END def __init__()

    def mouseMoveEvent(self, event):
        """
        Event handler that catches moving mouse events.

        @param event: QMouseEvent, class contains parameters that describe
                      a mouse event
        """
        ## we are only interested in middle mouse movements - maya style ;)
        if event.buttons() != QtCore.Qt.MiddleButton:
            return
        # END if

        ## mimeData container,
        ## for a mime base drag and drop transfer
        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)

        drag.setHotSpot(event.pos() - self.rect().topLeft())
        dropAction = drag.start(QtCore.Qt.MoveAction)
    # END def mouseMoveEvent()

    def mousePressEvent(self, event):
        """
        Event handler that catches mouse press events.
        @param event: QMouseEvent, class contains parameters that describe
                      a mouse event
        """
        QtGui.QToolButton.mousePressEvent(self, event)
        parent = self.parent()
        parent.set_dragged_button(self.text())
    # END def mousePressEvent()

    def set_order(self, order):
        """
        Sets the order in which the button is to be displayed
        @param order: int, oder number
        """
        self.order = order
    # END def set_order()

    def get_order(self):
        """
        Gets the order in which the button is to be displayed
        @return int, order number
        """
        return self.order
    # END def get_order()
# END class DraggableButton()
