#!/usr/bin/python
#
# Fix gpac compilation for OSX
# 

import os
import sys


def fix_gpac_configure(options, buildout):
	""" Fix gpac building """
	os.system("chmod u+x configure")
	if sys.platform == "darwin": # OSX specific fix
		print "Patching gpac for OSX"
		os.system("find . -name os_net.c | xargs perl -pi -e 's/u_long/unsigned long/g'")
	print "Done"

def fix_gpac_make(options, buildout):
	""" Fix ugly Mozilla dependency which cannot be disabled via configure """
	if sys.platform == "linux2":
		print "Patching gpac for Linux"
		os.system("find . -print0 | grep -FzZ applications/Makefile | xargs perl -pi -e 's/INSTDIRS\\+\\=osmozilla/#INSTDIRS+=osmozilla/g'")
		os.system("find . -print0 | grep -FzZ applications/Makefile | xargs perl -pi -e 's/APPDIRS\\+\\=osmozilla/#APPDIRS+=osmozilla/g'")
			
	print "Done"
