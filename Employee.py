#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProjectManagment import Project
from ProjectManagment import Task

class Employee(object):
	def Employee(self):
		pass

	def getName(self):
		return self.___name

	def setName(self, aName):
		"""@ReturnType void"""
		self.___name = aName

	def __init__(self):
		self.___name = None
		self._unnamed_Project_ = None
		"""@AttributeType ProjectManagment.Project
		# @AssociationType ProjectManagment.Project
		# @AssociationMultiplicity 1"""
		self._unnamed_Task_ = None
		"""@AttributeType ProjectManagment.Task
		# @AssociationType ProjectManagment.Task
		# @AssociationMultiplicity 1"""

