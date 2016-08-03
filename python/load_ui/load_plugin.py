""" 
#    @path        D:\Programare\Python\Tutorials Scripts\PySide\
#    @file        InterfacePlugin.py
#    @brief       This script create a interface.
#    @author      remus_avram
#    @date        05.2014
"""


import os
from loadUiType import loadUiType


# keep the path to the uiFile in a variable
uiFile = os.path.join(os.path.dirname(__file__), 'test.ui')

# keep the changeable names in variables
windowObject = 'PluginWindow'

base_class, form_class = loadUiType(uiFile)


class InterfacePluginCass(base_class, form_class):
	"""The super class for the Asset Manager, the Scene Manager and the
	Constructor Manager.
	"""
	
	def __init__(self, title='InterfacePluginCass'):
		"""Initializes the manager.
		@param title: the window title
		@type title: String
		
		"""
		super(InterfacePluginCass, self).__init__(qtutils.getMayaWindow())
		self.setupUi(self)