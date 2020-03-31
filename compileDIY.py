"""===============================================================================================================================================================
	
	這是關於 Python 使用 C/C++ 加速系列:

		
		compiler 預設 :
			Linux :  gcc/g++

			Max(Darwin) : clang

			Windows : MSVC cl
	
	




============================================================================================================================================================="""
import os 
import platform
import subprocess
import shutil


class ComplieDIY:
	def __init__(self):
		# 回傳作業系統名稱  Windows/Darwin(Mac)/Linux
		self.PlatformName = platform.system()
	#---------------------------------------------------------------------
	# cython
	def cython_copy2pyx(self,pyfile,source):
	    pyfilename1 = "{}{}".format(source,pyfile)
	    pyfilename2 = pyfile
	    shutil.copyfile(pyfilename1,pyfilename2)
	    pyfilename3 = pyfilename2.split(".py")[0]+".pyx"
	    os.rename(pyfilename2,pyfilename3)
	    print("copy + rename {} to {} !!".format(pyfilename1,pyfilename3))
	    return pyfilename3


	def cython_c2o(self,cfile):
		if self.PlatformName == "Linux":
			ofile = "{}.o".format(cfile.split(".c")[0])
			commands = [
				"gcc",
				"-pthread",
				"-DNDEBUG",
				"-g",
				"-fwrapv",
				"-O2",
				"-Wall",
				"-g",
				"-fstack-protector-strong", 
				"-Wformat",
				"-Werror=format-security",
				"-Wdate-time",
				"-D_FORTIFY_SOURCE=2",
				"-fPIC",
				"-I/usr/include/python3.6m",  # python3.6m
				"-c",
				cfile,
				"-o",
				"{}".format(ofile)
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return ofile 

		elif self.PlatformName == "Darwin":



		else:
			pass

	def cython_o2so(self,ofile):
		if self.PlatformName == "Linux":
			sofile = "{}.so".format(ofile.split(".o")[0])
			commands = [
				"gcc",
				"-pthread",
				"-shared",
				"-Wl,-O1",
				"-Wl,-Bsymbolic-functions",
				"-Wl,-Bsymbolic-functions",
				"-Wl,-z,relro",
				"-Wl,-Bsymbolic-functions",
				"-Wl,-z,relro",
				"-g",
				"-fstack-protector-strong",
				"-Wformat",
				"-Werror=format-security",
				"-Wdate-time",
				"-D_FORTIFY_SOURCE=2",
				"{}".format(ofile),
				"-o",
				"{}".format(sofile)
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return sofile
		elif self.PlatformName == "Darwin":



		else:
			pass

	def cython(self,pyfile,source="../"):
		pyxfile = self.cython_copy2pyx(pyfile,source=source)
		subprocess.run(["cython","-3",pyxfile]) # python3
		cfile = pyfile.split(".py")[0]+".c"
		ofile = self.cython_c2o(cfile)
		sofile = self.cython_o2so(ofile)
		print("[cython] {} --> {} --> {} --> {} --> {}".format(pyfile,pyxfile,cfile,ofile,sofile))


	

	#---------------------------------------------------------------------
	# ctypes 系列
	def ctypes_cpp2o(self,cppfile):
		if self.PlatformName == "Linux":
			ofile = "{}.o".format(cppfile.split(".cpp")[0])
			commands = [
				"gcc",
				"-pthread",
				"-DNDEBUG",
				"-g",
				"-fwrapv",
				"-O2",
				"-Wall",
				"-g",
				"-fstack-protector-strong",
				"-Wformat",
				"-Werror=format-security",
				"-Wdate-time",
				"-D_FORTIFY_SOURCE=2", 
				"-fPIC",
				"-I.",
				"-I/usr/include/python3.6m",
				"-c",
				cppfile,
				"-o",
				"{}".format(ofile),
				"-std=c++11"
			]
			print(" ".join(commands))
			subprocess.run(commands)
			return ofile



	def ctypes_o2so(self,ofile):
		if self.PlatformName == "Linux":
			sofile = "{}.so".format(ofile.split(".o")[0])
			commands = [
				"g++",
				"-pthread",
				"-shared",
				"-Wl,-O1",
				"-Wl,-Bsymbolic-functions",
				"-Wl,-Bsymbolic-functions", 
				"-Wl,-z,relro",
				"-Wl,-Bsymbolic-functions",
				"-Wl,-z,relro",
				"-g",
				"-fstack-protector-strong",
				"-Wformat",
				"-Werror=format-security",
				"-Wdate-time",
				"-D_FORTIFY_SOURCE=2",
				"{}".format(ofile),
				"-o",
				"{}".format(sofile)
			]
			print(" ".join(commands))
			subprocess.run(commands)
			return sofile


	def ctypes(self,cppfile):
		ofile = self.ctypes_cpp2o(cppfile)
		sofile = self.ctypes_o2so(ofile)
		print("[ctypes] {} --> {} --> {}".format(cppfile,ofile,sofile))





	








	
	



















	





if __name__ == '__main__':
	pass
		