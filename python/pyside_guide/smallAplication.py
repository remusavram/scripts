"""
@brief         This script imports a ui file converted to py.
                It's creating a menu and a toolBar.
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.14
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import mainWindowSmallApplication


class mainWindow(QMainWindow, mainWindowSmallApplication.Ui_MainWindow):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # self.connect(self.actionExit, SIGNAL("triggered()"), self.exitApp)
        self.actionExit.triggered.connect(self.exitApp)
    # END def __init__
    
    def exitApp(self):
        sys.exit(0)
    # END def exitApp
    
# END class smallApplication



def main():
    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if