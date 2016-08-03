'''
@package   fader    
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui


class FaderWidget(QtGui.QWidget):
    '''Fades between tow widgets'''
    
    def __init__(self, old_widget, new_widget=None, duration=1000, reverse=False):
        QtGui.QWidget.__init__(self, new_widget)
        
        self.resize(old_widget.size())
        
        self.old_pixmap = QtGui.QPixmap(old_widget.size())
        old_widget.render(self.old_pixmap)
        
        self.pixmap_opacity = 1.0
        
        self.timeline = QtCore.QTimeLine()
        if reverse:
            self.timeline.setDirection(self.timeline.Backward)
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.deleteLater)
        self.timeline.setDirection(duration)
        
        self.timeline.start()
        self.show()
    # END def __init__
    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    # END def paintEvent
    
    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()
        self.update()
    # END def animate
# END class FaderWidget


class FaderExample(QtGui.QWidget):
    '''
    Example widget using a FaderWidget to transition
    between two simple colored QWdgets in a stack layout.
    '''
    def __init__(self):
        super(FaderExample, self).__init__()
        
        self.resize(600,600)
        self.vlayout = QtGui.QVBoxLayout(self)
        
        self.w1 = QtGui.QWidget()
        self.w1.setStyleSheet("QWidget {background-color: blue;}")
        self.w2 = QtGui.QWidget()
        self.w2.setStyleSheet("QWidget {background-color: red;}") 
        
        self.stacked = QtGui.QStackedLayout()
        self.stacked.addWidget(self.w1)
        self.stacked.addWidget(self.w2)
        
        self.vlayout.addLayout(self.stacked)
        self.fadeButton = QtGui.QPushButton("Fade")
        self.resetButton = QtGui.QPushButton("Reset")
        
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.fadeButton)
        buttonLayout.addWidget(self.resetButton)
        
        self.vlayout.addLayout(buttonLayout)
        
        self.fadeButton.clicked.connect(self.fade)
        self.resetButton.clicked.connect(self.reset)
    # END def __init__

    def fade(self):
        FaderWidget(self.w1, self.w2)
        self.stacked.setCurrentWidget(self.w2)
    # END def fade
    
    def reset(self):
        self.stacked.setCurrentWidget(self.w1)
    # END def reset
# END class FaderExample

'''
Run in Maya:

================================================================================
import sys
from PyQt4 import QtGui

pathToDir = r"D:\Programare\PySide-PyQt\Tutorials\cmivfx - PyQt4 UI Development for Maya\PyQt for Maya"

if pathToDir not in sys.path:
    sys.path.append(pathToDir)

try:
    reload(fader)
except:
    import fader

f = fader.FaderExample()
f.show()
================================================================================
'''
