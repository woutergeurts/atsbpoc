#!/usr/bin/python
import sys
from atsb_vt import atsb_vt

class atsb_parse:
	""" documentation """
	m_delimiter = ";"
	def __init__ (self, DSO):
		m_ean = atsb_vt(atsb_vt.ean, DSO)
		m_mc  = atsb_vt(atsb_vt.mc, DSO)
		m_dso = DSO
		
	def parsefile(self,input, output, filetype):
		with open(input,"r") as fp_in:
			with open(output, "w") as fp_out:
				for line in fp_in:
					# TBD deal with \n\r; 15m
					x = [value for value in line.split(
						self.m_delimiter)]
					y = transform(x,filetype)
					fp_out.write(self.m_delimiter.join(y))
					
		
def transform(x,type):
	switcher = { 
		'test': transform_test,
		'testing': transform_testing,
	}
	return switcher.get(type)(x)

def transform_test(x):
	x[0] = 'noot'
	x[1] = 'aap'
	return x

def transform_testing(x):
	x[0] = 'nut'
	x[1] = 'monkey'
	return x

if __name__ == "__main__":
	a = atsb_parse("aap")
	a.parsefile('test/parse.csv', 'test/parse_out.csv', 'test')
	a.parsefile('test/parse.csv', 'test/parse_out2.csv', 'testing')
