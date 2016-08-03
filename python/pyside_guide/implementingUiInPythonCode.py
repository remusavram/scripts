"""
@brief         This script implement an UI in Python Code
                Command to convert x.ui in x.py: 
                pyside-uic.exe .\GUI\showDialog.ui -o showGui.py
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.09
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import showGui


class MainDialog(QDialog, showGui.Ui_mainDialog):
    """ This class will use use Ui_mainDialog from showGui. """
    
    def __init__(self, parent=None):
        """ This method is a constructor. """
        
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.connect(self.showButton, SIGNAL("clicked()"), self.showMessageBox)
    # END def __init__
    
    def showMessageBox(self):
        """ This method returns a short message. """
        
        QMessageBox.information(self, "Hello", "Hello there, " + self.nameEdit.text())
    # END def showMessageBox   
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