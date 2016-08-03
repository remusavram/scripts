"""
@brief         This script imports a ui file converted to py.
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.14
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import pickAnOS



class mainDialog(QDialog, pickAnOS.Ui_mainDialog):
    
    def __init__(self, parent=None):
        super(mainDialog, self).__init__(parent)
        self.setupUi(self)
    # END def __init__
# END class mainDialog



def main():
    app = QApplication(sys.argv)
    form = mainDialog()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if