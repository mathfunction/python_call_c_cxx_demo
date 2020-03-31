

import os
from compileDIY import *


if __name__ == '__main__':
	ROOTPATH = os.path.dirname(os.path.abspath(__file__))
	"""
	os.chdir("./cython")
	cython_compile("pythonFunc.py","../python/")
	os.chdir(ROOTPATH)
	"""

	os.chdir("./ctypes")
	ctypes_compile("cxxFunc.cpp")
	
	os.chdir(ROOTPATH)