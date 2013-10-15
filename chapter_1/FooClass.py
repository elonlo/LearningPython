#!/usr/bin/env python
class FooClass(object):
	"""my very first class: FooClass"""
	version = 0.1 #class (data) attribute
	def __init__(self, nm = 'John Doe'):
		"""constructor"""
		self.name = nm #class instance (data) attribute
		print ' Created a class instance for', nm
	def showname(self):
		"""display instance attribute and class name"""
		print 'Your name is ', self.name
		print 'My name is ', self.__class__.__name__
	def showver(self):
		"""display class (static) attribute and class name"""
		print self.version			
	def addMe2Me(self, x):
		"""apply + operation to argument"""
		return x + x

#fool = FooClass()
#fool.showname()
#fool.showver()
#print fool.addMe2Me(5)
#print fool.addMe2Me('xyz')


	
