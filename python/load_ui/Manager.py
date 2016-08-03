


class Manager(base_class, form_class):
	"""The super class for the Asset Manager, the Scene Manager and the
	Constructor Manager.
	"""
	
	def __init__(self, title='Manager'):
		"""Initializes the manager.
		@param title: the window title
		@type title: String
		
		"""
		super(Manager, self).__init__(qtutils.getMayaWindow())
		self.setupUi(self)
	