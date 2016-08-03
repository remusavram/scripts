#!/usr/bin/python

'''
@package   basicListComboboxWithModel
@brief     Creates a combobox with model view controller
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
    data << "one" << "two" << "three" << "four"
    
    listView = QtGui.QListView()
    listView.show()
    
    model = QtGui.QStringListModel(data)
    
    listView.setModel(model)
    
    comboBox = QtGui.QComboBox()
    comboBox.setModel(model)
    comboBox.show()
    
    listView2 = QtGui.QListView()
    listView2.show()
    listView2.setModel(model)
    
    
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__': main()