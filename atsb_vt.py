#!/usr/bin/python
class atsb_vt:
	""" documentation """
	ean = "A.01"
	mc = "M.101"
	m_table = {}
	
	def __init__ (self,type,DSO):
		self.m_dso = DSO
		self.m_type = type
		# hier moet en undump komen van de file, voor herstarten
		
	def get(self,input):
		if not(input in atsb_vt.m_table):
			self.m_table[input] = anonimize(
				input,self.m_dso,self.m_type)
		return self.m_table[input]

	def dump(self):
		# TBD voor dumpen is een simpele python manier
		return "vt {0} voor {1} dumped".format(self.m_type,self.m_dso)


def anonimize(input,dso,type):
	# hier moet een slimme lookup op basis van DSO, prefix etc komen
	# TBD: voor anonimiseren van MC is de bijbehorende EAN nodig!!, 
	# check of dat altijd kan
	print "anonimize", input, dso, type
	return input+1;

if __name__ == "__main__":
	a = atsb_vt(atsb_vt.ean, "aap")
	print a.get(41)
	print a.get(41)
	print a.get(43)
	print a.dump()
