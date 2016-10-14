#!/usr/bin/python
import sys
import os
import re
from atsb_vt import atsb_vt
from atsb_parse import atsb_parse

def main():
	global lf
	source_dir = sys.argv[1]
	target_dir = sys.argv[2]
	logfile    = sys.argv[3]
	todosuffix = ".todo"
	donesuffix = ".done"
	#
	# TBD: check validity; 10min
	#
	# TBD: create log class; 45min
	lf = open(logfile, 'w')
	tdf = open(logfile + todosuffix, 'w')
	produce_worklist(source_dir, target_dir, tdf)
	tdf.close()
	tdf = open(logfile + todosuffix, 'r')
	donef = open(logfile + donesuffix, 'w')
	run_worklist(tdf,donef)

def produce_worklist(source_dir, target_dir, tdf):
	# TBD automate documentation generation; 2 h
	""" The worklist or todo file (tdf) provides instant overview of the 
	work. It provides the parameters to be passed to the parse routine
	and some information on lines in the file, to produce a progress 
	report
	format
	<command> <source> <target> <size>
	command = cp, parse_<type>, size = wc
	"""
	# TBD: create
	# walk source_dir and create mkdir -p target dir
	os.chdir(source_dir)
	for dir_name, subdir_list, file_list in os.walk("."):
		for fname in file_list:
			command = "ignore"
			filetype = "_"
			m = re.match( r'[0-9]+_([A-Z]+)_.*', fname)
			if m:
				command = "parse"
				filetype = m.group(1)
			source = source_dir + '/' + dir_name + '/' + fname
			target = target_dir + '/' + dir_name + '/' + fname
			ensure_dir(target)
			size = os.popen("wc -l " + dir_name + '/' + fname).read() 
			tdf.write('{0} {1} {2} {3} {4}'.format(
				command, filetype, source, target, size ))
			
	os.chdir('..')

def ensure_dir(f):
	d = "../" + os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

#
def run_worklist(tdf,donef):
#	progress to tdf and donef simultaneously to get to the restart point
#	run command and add entry to donef
#
	# TBD: assumption that all files belong to same DSO!!
	parser = atsb_parse("TESTDSO")
	for line in tdf:
		# TBD refactor for readibility; 30 min
		[command,filetype,source,target,size,tmp] = [value for value in line.split(' ')]
		if command == 'parse':
			parser.parsefile(source, target, 'test')

		donef.write('{0};{1};{2};{3}'.format(
			command, filetype, source, target ))

def write_log(string):
	# TBD: add timestamp
	global lf
	lf.write(string + '\n')

if __name__ == '__main__':
	main()
