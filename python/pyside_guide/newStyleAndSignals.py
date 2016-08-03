"""
@brief         This script we will use new signals and slots.
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.14
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys


class MainDialog(QDialog):
    
    myOwnSignal = Signal((int,), (str,))
    
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        
        self.btn1 = QPushButton("Button")
        
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)
        
        #self.connect(self.btn1, SIGNAL("clicked()"), self.btn1clicked)
        # or
        self.btn1.clicked.connect(self.btn1clicked)
        
        self.myOwnSignal.connect(self.myOwnSignalEmitted)
        self.myOwnSignal[str].connect(self.myOwnSignalEmitted)
        
        #self.connect(self, SIGNAL("myOwnSignal()"), self.myOwnSignalEmitted)
    # END def __init__

    def btn1clicked(self):
        #QMessageBox.information(self, "Hello", "Buntton 1 clicked!")
        #self.emit(SIGNAL("myOwnSignal()"))
        self.myOwnSignal[str].emit("Whatever!")
        pass
    # END def btn1clicked
    
    def myOwnSignalEmitted(self, param):
        print "SIGNAL EMMINTED! " + str(param)
        print type(param)
    # END def myOwnSingnal
# END class MainDialog




def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if