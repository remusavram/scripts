'''
@package   slider    
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui
from ui import resources_rc


class Slider(QtGui.QSlider):
    '''A QSkuder with a custom stylesheet'''
    
    def __init__(self, *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        
        self.setStyleSheet('''
            QSlider::groove:horizontal {
                border: 1px inset qlineargradlent(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #848484);
                border-radius: 6px;
                height: 10px;
                background: qlineargradient(x1:0, y1:0, y2:1, stop:0 #848484, stop:1 #919191);
                margin: 2px 6px;
            }
            
            QSlider::handle:horizontal {
                background-color: rgba(0,0,0,0);
                image: url(:/images/metal-volume-button-template.jpg);
                border: 8px;
                width: 18px;
                margin: -6px;
                border-radius: 0px;
            }
        ''')

        self.setMinimumHeight(18)
    # END def __init__
# END class Slider


class SliderExample(QtGui.QWidget):
    '''Compares a standard QSlider to a custom Slider'''
    
    def __init__(self):
        super(SliderExample, self).__init__()
        self.resize(300,100)
        
        layout = QtGui.QVBoxLayout(self)
        
        slider1 = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider2 = Slider(QtCore.Qt.Horizontal)
        
        layout.addWidget(slider1)
        layout.addWidget(slider2)
    # END def __init__
# END class SliderExample


'''
Start in Maya:

================================================================================
import sys
from PyQt4 import QtGui

pathToDir = r"D:\Programare\PySide-PyQt\Tutorials\cmivfx - PyQt4 UI Development for Maya\PyQt for Maya"

if pathToDir not in sys.path:
    sys.path.append(pathToDir)

try:
    reload(slider)
except:
    import slider

slid = slider.SliderExample()
slid.show()
================================================================================
'''
