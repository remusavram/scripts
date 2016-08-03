#!/usr/python

"""
@brief         Simple Dialog Application
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.04
"""


from PySide.QtCore import *
from PySide.QtGui import *
import sys


__appName__ = "Dumb Dialogs"



class Program(QDialog):
	""" This class ..."""
	
	def __init__(self, parent=None):
		""" Constructor class."""
		
		super(Program, self).__init__()
		
		self.setWindowTitle(__appName__)
		
		btn = QPushButton("Open Dialog")
		self.label1 = QLabel("Label 1 Result")
		self.label2 = QLabel("Label 2 Result")
		
		layout = QVBoxLayout()
		layout.addWidget(btn)
		layout.addWidget(self.label1)
		layout.addWidget(self.label2)
		self.setLayout(layout)
		
		self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)
	# END def __init__
	
	def dialogOpen(self):
		""" Open the dialog window. """
		
		dialog = Dialog()
		if dialog.exec_():
			self.label1.setText("Spinbox value is " + str(dialog.spinBox.value()))
			self.label2.setText("Checkbox is " + str(dialog.checkBox.isChecked()))
		else:
			QMessageBox.warning(self, __appName__, "Dialog canceled!")
	# END def dialogOpen
# END class Program



class Dialog(QDialog):
	""" This class ..."""
	
	def __init__(self, parent=None):
		""" Constructor. """
		
		super(Dialog, self).__init__(parent)
		
		self.setWindowTitle("Dialog")
		
		self.checkBox = QCheckBox("Check me out!")
		self.spinBox = QSpinBox()
		buttonOK = QPushButton("OK")
		buttonCancel = QPushButton("Cancel")
		
		layout = QGridLayout()
		layout.addWidget(self.spinBox, 0, 0)
		layout.addWidget(self.checkBox, 0, 1)
		layout.addWidget(buttonOK)
		layout.addWidget(buttonCancel)
		self.setLayout(layout)
		
		self.connect(buttonOK, SIGNAL("clicked()"), self, SLOT("accept()"))
		self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
	# END __init__ def
# END calss Dialog



def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if