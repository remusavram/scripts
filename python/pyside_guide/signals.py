"""
@brief         Simple Signals and Slots
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.04
"""


from PySide.QtCore import *
from PySide.QtGui import *
import sys



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)

        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.setWindowTitle("Signals and Slots")


    # END def __init__
# END class Form


def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if



print '\n\n\nFinish Successfully!'