#!/usr/bin/python
#
# Fix gpac compilation for OSX
# 

import os
import sys


def fix_gpac(options, buildout):
	print "Patching gpac for OSX"
	os.system("chmod u+x configure")
	if sys.platform == "darwin": # OSX specific fix
		os.system("find . -name os_net.c | xargs perl -pi -e 's/u_long/unsigned long/g'")
	print "Done"