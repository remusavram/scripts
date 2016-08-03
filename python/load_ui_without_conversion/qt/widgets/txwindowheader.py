#-*-coding:utf-8-*-
"""
@package tx_common.qt.widgets.txwindowheader
@brief Header for the Trixter Tools

@author Paul Schweizer
@email paul.schweizer@trixter.de
@copyright 2014 TRIXTER Film GmbH
"""
__all__ = ['TXWindowHeader']

from PySide import QtCore, QtGui
from tx import path
from tx_common import qt


tx_win_form_class, tx_win_base_class = qt.utils.loadUiType(path.Path(__file__).dirname().dirname() /
                                                          'resource' / 'txwindowheader.ui')


class TXWindowHeader(tx_win_base_class, tx_win_form_class):

    """A header for the Trixter Tools."""

    def __init__(self, title):
        """Initializes the header.
        Creates the labels, sets the title and the Trixter logo.
        @param title: the title of the window
        @type title: String
        """
        super(TXWindowHeader, self).__init__()
        self.setupUi(self)
        self.window_lbl.setText(title)
        pxm = QtGui.QPixmap(path.Path(__file__).dirname().dirname() / 'resource' / 'tx_x.png').scaled(30, 30, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.tx_logo_lbl.setPixmap(pxm)
    # END def __init__
# END class TXWindowHeader
