


import timeit
import os
import sys
from compileDIY import *


if __name__ == '__main__':
	ROOTPATH = os.path.dirname(os.path.abspath(__file__))
	try:
		if sys.argv[1] == "--compile-cython":
			
			os.chdir("./cython")
			cython_compile("pythonFunc.py","../python/")
			os.chdir(ROOTPATH)
		if sys.argv[1] == "--compile-ctypes":
			os.chdir("./ctypes")
			ctypes_compile("cxxFunc.cpp")
			os.chdir(ROOTPATH)
		if  sys.argv[1] == "--run-python":
			E = {
				"A-B":2,
				"A-C":3,
				"C-E":10,
				"A-D":11,
				"B-D":2,
				"C-A":12,
				"A-E":13,
				"A-Z":2,
				"G-H":1,
				"C-G":5,
				"D-C":10,
				"A-D":2,
				"R-A":3,
				"T-D":12,
				"C-H":17,
				"B-X":10,
				"X-T":1,
				"E-Q":3,
				"U-V":1,
				"V-A":2,
				"V-B":3,
				"C-A":2,
				"E-A":12,
				"B-C":100,
				"D-A":2,
				"A-S":3,
				"S-Q":1,
				"Q-A":2
			}
			sys.path.append("./python/")
			import pythonFunc
			t1 = timeit.default_timer()
			print(pythonFunc.MonteCarloPi(1000000))
			result  = pythonFunc.Floyd_Warshall_Algorithm(E)
			t2 = timeit.default_timer()
			print("{} ms".format(1000*(t2-t1)))
			print(result[1])
			print(result[0])
		if sys.argv[1] == "--run-cython":
			E = {
				"A-B":2,
				"A-C":3,
				"C-E":10,
				"A-D":11,
				"B-D":2,
				"C-A":12,
				"A-E":13,
				"A-Z":2,
				"G-H":1,
				"C-G":5,
				"D-C":10,
				"A-D":2,
				"R-A":3,
				"T-D":12,
				"C-H":17,
				"B-X":10,
				"X-T":1,
				"E-Q":3,
				"U-V":1,
				"V-A":2,
				"V-B":3,
				"C-A":2,
				"E-A":12,
				"B-C":100,
				"D-A":2,
				"A-S":3,
				"S-Q":1,
				"Q-A":2
			}
			sys.path.append("./cython/")
			import pythonFunc
			t1 = timeit.default_timer()
			print(pythonFunc.MonteCarloPi(1000000))
			result  = pythonFunc.Floyd_Warshall_Algorithm(E)
			t2 = timeit.default_timer()
			print("{} ms".format(1000*(t2-t1)))
			print(result[1])
			print(result[0])


	except Exception as e:
		print(e)



	
