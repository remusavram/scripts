#!/usr/bin/python

'''
@package   dialog_validation  
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''


from PyQt4 import QtCore, QtGui, uic
import sys
from os import path


# CONFIGURATION
MAIN_UI_FILE = path.join(path.dirname(__file__), 'resource/infoAboutYou.ui')
INFO_UI_FILE = path.join(path.dirname(__file__), 'resource/infoDialog.ui')


class MainWindow(QtGui.QMainWindow):
    """ This class connects the fields form login.ui with commands. """
    
    def __init__(self):
        """ Initializes MainWindow."""
        super(MainWindow, self).__init__()
        # load UI
        uic.loadUi(MAIN_UI_FILE, self)
        
        self.setInfoDumbButton.clicked.connect(self.show_dumb_dialog)
        self.setInfoSmartButton.clicked.connect(self.show_smart_dialog)
    # END def __init__
    
    def show_smart_dialog(self):
        dialog = SmartInfoDialog()
        
        if dialog.exec_() == dialog.Accepted:
            self.process_dialog(dialog)
    # END def show_smart_dialog
    
    def show_dumb_dialog(self):
        dialog = DumbInfoDialog()
        
        while True:
            if dialog.exec_() == dialog.Accepted:
                
                first = dialog.firstNameLineEdit.text()
                last  = dialog.lastNameLineEdit.text()
                email = dialog.emailLineEdit.text()
                
                if not (first and last and email):
                    err = "All fields are required"
                    QtGui.QMessageBox.warning(self, "Error in form", err)
                    continue
                self.process_dialog(dialog)
            break
    # END def show_dumb_dialog
    
    def process_dialog(self, dialog):
        ''' Pricess a dialog widget as-is and update display'''
        
        first = dialog.firstNameLineEdit.text()
        last  = dialog.lastNameLineEdit.text()
        email = dialog.emailLineEdit.text()
        age   = dialog.ageSpinBox.value()
        
        plural = (age > 1) and 's' or ''
        
        msg = '''
            Hi, %(first)s %(last)s! <br>
            Your E-Mail Address is %(email)s <br>
            And you are %(age)s year %(plural)s old!
            ''' % locals()
        
        self.infoLabel.setText(msg)
    # END def process_dialog
# END class MainWindow


class DumbInfoDialog(QtGui.QDialog):
    ''' A simple dialog widget with no logic.'''
    def __init__(self):
        super(DumbInfoDialog, self).__init__()
        # load UI
        uic.loadUi(INFO_UI_FILE, self)
    # END def __init__
# END class DumbInfoDialog

class SmartInfoDialog(DumbInfoDialog):
    ''' Subclass of DumbInfoDialog
        Adds fields validators, and form validation during the accept action.'''
    def __init__(self):
        super(SmartInfoDialog, self).__init__()
        
        self._email_rx = QtCore.QRegExp(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$',
                                       QtCore.Qt.CaseInsensitive)
        self.emailLineEdit.setValidator(QtGui.QRegExpValidator(self._email_rx, self))
    # END def __init__
    
    def accept(self):
        err = ''
        if not (self.firstNameLineEdit.text() and self.lastNameLineEdit.text()):
            err = 'First and Last name fields are required'
        elif not self._email_rx.exactMatch(self.emailLineEdit.text()):
            err = 'Email address is not valid'
        
        if err:
            QtGui.QMessageBox.warning(self, 'Error is from', err)
            return
        super(SmartInfoDialog, self).accept()
    # END def accept
# END class SmartInfoDialog
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
# END def main

if __name__ == '__main__': main()
