#-*-coding:utf-8-*-
"""
@package tx_common.qt.utils.widgets.flowlayout
@brief A flow layout for qt

@author Sascha Kremers
@email sascha.kremers@trixter.de
@copyright 2013 TRIXTER Film GmbH
"""
__all__ = ['FlowLayout']

from PySide import QtCore, QtGui


class FlowLayout(QtGui.QLayout):
    """A custom flow layout"""
    def __init__(self, parent=None, margin=0, spacing=0):
        """
        @param parent:
        @param margin:
        @param spacing:
        """
        super(FlowLayout, self).__init__(parent)
        if parent is not None:
            self.setMargin(margin)
        self.setSpacing(spacing)
        self.itemList = []
    # END def __init__()

    def __del__(self):
        """
        Garbage collection fun, called when reference count reaches zero
        """
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)
        # END while item
    # END def __del__()

    def addItem(self, item):
        """
        Add item to the itemlist
        @param item: QLayoutItem
        """
        self.itemList.append(item)
    # END def addItem()

    def count(self):
        """
        Return number of items in layout
        @return int
        """
        return len(self.itemList)
    # END def count()

    def itemAt(self, index):
        """
        @param index: int, order number
        @return QLayutItem
        """
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]
        # END if

        return None
    # END def itemAt()

    def takeAt(self, index):
        """
        Remove item at given index from itemlist
        @param index: int, order number
        @return QLayoutItem
        """
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        # END if

        return None
    # END def takeAt()

    def expandingDirections(self):
        """
        @return Qt.Orientations
        """
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))
    # END def expandingDirections()

    def hasHeightForWidth(self):
        """
        @return bool
        """
        return True
    # END def hasHeightForWidth()

    def heightForWidth(self, width):
        """
        Return the height for the given width
        @param width: int width size of the layout
        @return int
        """
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height
    # END def heightForWidth()

    def setGeometry(self, rect):
        """
        SetGeometry for the layout
        @param rect: QRect
        """
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)
    # END def setGeometry()

    def sizeHint(self):
        """
        @return QSize
        """
        return self.minimumSize()
    # END def sizeHint()

    def minimumSize(self):
        """
        Determine the minimumSize for the layout,
        by collecting the minimumSize for every item.
        @return QSize
        """
        size = QtCore.QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
        # END for item in self.itemList

        return size
    # END def minimumSize()

    def doLayout(self, rect, testOnly):
        """
        Calculate the height for the layout and set it to geometry if needed
        @param rect: QRect
        @param testOnly: bool, if true do not setGeometry
        """
        ## determine x and y position
        x = rect.x()
        y = rect.y()

        lineHeight = 0
        for item in self.itemList:
            wid = item.widget()

            ## get horizontal and vertical spacing for the widget
            h_spacing = wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton,
                                                  QtGui.QSizePolicy.PushButton,
                                                  QtCore.Qt.Horizontal)
            v_spacing = wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton,
                                                  QtGui.QSizePolicy.PushButton,
                                                  QtCore.Qt.Vertical)

            ## spacing = layout spacing + item spacing
            spaceX = self.spacing() + h_spacing
            spaceY = self.spacing() + v_spacing

            nextX = x + item.sizeHint().width() + spaceX

            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0
            # END if

            ## when testOnly we do not want to modify the geometry
            ## of the layout
            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y),
                                 item.sizeHint()))
            # END if

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())
        # END for item in self.itemlist

        return y + lineHeight - rect.y()
    # END def doLayout()
# END class FlowLayout()
