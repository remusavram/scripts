#!/usr/bin/python

'''
@package   basicListCombobox
@brief     Creates a basic list combobox
@details
@title     PyQt4 Model View Tutorial Part 01
@URL       https://www.youtube.com/watch?v=mCHVI8OXDxw&list=PL8B63F2091D787896
@author    Remus Avram
@date      2014.12
'''


from PyQt4 import QtGui, QtCore, uic
import sys


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    
    # DATA
    data = QtCore.QStringList()
    data << "one" << "two"
    
    # LISTWIDGET
    listWidget = QtGui.QListWidget()
    listWidget.show()
    listWidget.addItems(data)
    
    count = listWidget.count()
    for i in range(count):
        item = listWidget.item(i)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
    
    comboBox = QtGui.QComboBox()
    comboBox.show()
    comboBox.addItems(data)
    
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__': main()