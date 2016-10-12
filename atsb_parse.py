#!/usr/bin/python
class atsb_vt:
	""" documentation """
	m_table = {}
	def __init__ (self):
		print "init"
		
		
	def anonimize(self, ean):
		return ean+1	

if __name__ == "__main__":
	a = atsb_vt()
	print a.anonimize(3)
