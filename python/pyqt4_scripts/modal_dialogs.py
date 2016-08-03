#!/usr/bin/python

'''
@package   modal_dialogs   
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''


from PyQt4 import QtCore, QtGui
import sys

class Window(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        
        self.resize(300,200)
        
        self.layout = QtGui.QHBoxLayout(self)
        
        self.modalButton = QtGui.QRadioButton("Go modal")
        self.asyncModalButton = QtGui.QRadioButton("Go async modal")
        self.nonModalButton = QtGui.QRadioButton("Go non-modal")
        
        self.layout.addWidget(self.modalButton)
        self.layout.addWidget(self.asyncModalButton)
        self.layout.addWidget(self.nonModalButton)
        
        self.buttonGroup = QtGui.QButtonGroup()
        self.buttonGroup.setExclusive(True)
        
        self.buttonGroup.addButton(self.modalButton)
        self.buttonGroup.addButton(self.asyncModalButton)
        self.buttonGroup.addButton(self.nonModalButton)
        
        self.buttonGroup.buttonClicked['QAbstractButton*'].connect(self.handle_show_dialog)
    # END def __init__
    
    def handle_show_dialog(self, button):
        ''' slot to handle a radio button being clicked '''
        
        if button is self.modalButton:
            self.show_modal()
        elif button is self.asyncModalButton:
            self.show_model_async()
        elif button is self.nonModalButton:
            self.show_non_model()
        print "Finished running dialog slot"
    # END def handle_show_dialog
    
    def show_modal(self):
        dialog = self._get_dialog()
        ret = dialog.exec_()
        print "Return value from modal dialog was", ret
    # END def show_model
    
    def show_model_async(self):
        dialog = self._get_dialog()
        dialog.setModal(True)
        dialog.show()
        
        def handle_ret(ret):
            print "Return value from async modal dialog was", ret
        # END def handle_ret
        dialog.finished.connect(handle_ret)
    # END def show_model_async
                
    def show_non_model(self):
        dialog = self._get_dialog()
        dialog.show()
        
        def handle_ret(ret):
            print "Return value from async modal dialog was", ret
        # END def handle_ret
        dialog.finished.connect(handle_ret)
    # END def show_non_model
    
    def _get_dialog(self):
        ''' Private helper method to return a common test dialog'''
        dialog = QtGui.QDialog(self)
        dialog.resize(100,40)
        accept = QtGui.QPushButton("Accept", dialog)
        accept.clicked.connect(dialog.accept)
        return dialog
    # END def _get_dialog
# END class Window

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    win.raise_()
    sys.exit(app.exec_())

if __name__ == "__main__": main()
    
        