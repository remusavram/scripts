"""
@brief         This script dealing with threading.
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.11
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import time

# import modules from the same project
import showGui



class MainDialog(QDialog, showGui.Ui_mainDialog):
    """ This class will use use Ui_mainDialog from showGui. """
    
    def __init__(self, parent=None):
        """ This method is a constructor. """
        
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.showButton.setText("Process")
        self.connect(self.showButton, SIGNAL("clicked()"), self.processData)
        
        self.workerThread = WorkerThread()
        self.connect(self.workerThread, SIGNAL("threadDone(QString, QString)"), self.threadDone, Qt.DirectConnection)
    # END def __init__
    
    def processData(self):
        """ This method returns a short message. """
        
        self.workerThread.start()
        QMessageBox.information(self, "Done!", "Done.")
    # END def showMessageBox   
    
    def threadDone(self, confirmation1, confirmation2):
        #QMessageBox.warning(self, "Warning!", "Thread execution completed!")
        self.nameEdit.setText("Worker thread finished processing!")
        print confirmation1
        print confirmation2
    # END def threadDone
# END class MainDialog



class WorkerThread(QThread):
    """ This class ... """
    
    def __init__(self, parent=None):
        """ This method is a constructor. """
        
        super(WorkerThread, self).__init__(parent)
    
    def run(self):
        time.sleep(5)
        self.emit(SIGNAL("threadDone(QString, QString)"), "Confirmation that the thread is finished.", "The second confirmation!")
    
    
# END class WorkerThread



def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if