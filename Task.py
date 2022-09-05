#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProjectManagment import WorkBreakdownStructure
from ProjectManagment import Resources
from ProjectManagment import Employee

class Task(object):
	def Task(self):
		pass

	def getName(self):
		return self.___name

	def setName(self, aName):
		"""@ReturnType void"""
		self.___name = aName

	def getTheEmployees(self):
		return self.___theEmployees

	def getTheEmployees(self, aTheEmployees):
		"""@ReturnType void"""
		pass

	def getTheResources(self):
		return self.___theResources

	def setTheResources(self, aTheResources):
		"""@ReturnType void"""
		self.___theResources = aTheResources

	def __init__(self):
		self.___name = None
		self.___theEmployees = None
		self.___theResources = None
		self._unnamed_WorkBreakdownStructure_ = None
		"""@AttributeType ProjectManagment.WorkBreakdownStructure
		# @AssociationType ProjectManagment.WorkBreakdownStructure
		# @AssociationMultiplicity 1"""
		self._unnamed_Resources_ = []
		"""@AttributeType ProjectManagment.Resources*
		# @AssociationType ProjectManagment.Resources[]
		# @AssociationMultiplicity *"""
		self._unnamed_Employee_ = []
		"""@AttributeType ProjectManagment.Employee*
		# @AssociationType ProjectManagment.Employee[]
		# @AssociationMultiplicity *"""

