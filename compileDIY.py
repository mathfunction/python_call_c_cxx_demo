"""===============================================================================================================================================================
	
	這是關於 Python 使用 C/C++ 加速系列:

		
		- compiler 預設 :
			Linux :  GNU gcc/g++
			Max(Darwin) : clang/clang++
			Windows :  
				cython : MSYS2 : gcc.exe
				ctypes : MSVC :  cl.exe
	
		- commands 部分實作，需自行連結函式庫 !! 
	




============================================================================================================================================================="""
import os 
import platform
import subprocess
import shutil

class ComplieDIY:
	def __init__(self):
		# 回傳作業系統名稱  Windows/Darwin(Mac)/Linux
		self.PlatformName = platform.system()
	#======================================================================================================================================================================================================================
	# cython
	def cython_copy2pyx(self,pyfile,source):
	    pyfilename1 = "{}{}".format(source,pyfile)
	    pyfilename2 = pyfile
	    shutil.copyfile(pyfilename1,pyfilename2)
	    pyfilename3 = pyfilename2.split(".py")[0]+".pyx"
	    try:
	    	os.remove(pyfilename3)
	    except:
	    	pass
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
				ofile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return ofile 

		elif self.PlatformName == "Darwin":
			ofile = "{}.o".format(cfile.split(".c")[0])
			commands = [
				"clang",
				"-Wno-unused-result",
				"-Wsign-compare",
				"-Wunreachable-code",
				"-fno-common",
				"-dynamic",
				"-DNDEBUG",
				"-g", 
				"-fwrapv", 
				"-O3", 
				"-Wall", 
				"-isysroot",
				"/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk",
				"-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include", 
				"-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers", 
				"-I/usr/local/include -I/usr/local/opt/openssl/include", 
				"-I/usr/local/opt/sqlite/include", 
				"-I/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/include/python3.7m", 
				"-c", 
				cfile, 
				"-o", 
				ofile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return ofile
		
		elif self.PlatformName == "Windows":
			ofile = "{}.o".format(cfile.split(".c")[0])
			commands = [
				"gcc.exe",
				"-mdll",
				"-O", 
				"-Wall", 
				"-DMS_WIN64",
				"-IC:\\ProgramData\\Anaconda3\\include", 
				"-IC:\\ProgramData\\Anaconda3\\include",
				"-c", 
				cfile, 
				"-o",
				ofile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return ofile
		else:
			exit()


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
				ofile,
				"-o",
				sofile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return sofile	
		elif self.PlatformName == "Darwin":
			sofile = "{}.so".format(ofile.split(".o")[0])
			commands = [
				"clang",
				"-bundle",
				"-undefined", 
				"dynamic_lookup",
				"-isysroot",
				"/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk",
				ofile,
				"-L/usr/local/lib", 
				"-L/usr/local/opt/openssl/lib", 
				"-L/usr/local/opt/sqlite/lib",
				"-o",
				sofile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return sofile	
		elif self.PlatformName == "Windows":
			#deffile = "{}.def".format(ofile.split(".o")[0])
			pydfile = "{}.pyd".format(ofile.split(".o")[0])
			commands = [
				"gcc.exe",
				"-shared", 
				"-s", 
				ofile,
				"-LC:\\ProgramData\\Anaconda3\\libs",
				"-LC:\\ProgramData\\Anaconda3\\PCbuild\\amd64", 
				"-lpython36", 
				"-lmsvcr140",
				"-o",
				pydfile
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return pydfile
		else:
			exit()
		

	def cython(self,pyfile,source="../"):
		pyxfile = self.cython_copy2pyx(pyfile,source=source)
		subprocess.run(["cython","-3",pyxfile]) # python3
		cfile = pyfile.split(".py")[0]+".c"
		ofile = self.cython_c2o(cfile)
		sofile = self.cython_o2so(ofile)
		print("[cython] {} --> {} --> {} --> {} --> {}".format(pyfile,pyxfile,cfile,ofile,sofile))


	

	


	#======================================================================================================================================================================================================================
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
				ofile,
				"-std=c++11"
			]
			print(" ".join(commands))
			subprocess.run(commands)
			return ofile
		elif self.PlatformsName == "Darwin":
			ofile = "{}.o".format(cppfile.split(".cpp")[0])
			commands = [
				"clang",
				"-Wno-unused-result",
				"-Wsign-compare",
				"-Wunreachable-code",
				"-fno-common",
				"-dynamic",
				"-DNDEBUG",
				"-g",
				"-fwrapv",
				"-O3",
				"-Wall",
				"-isysroot",
				"/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk",
				"-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include", 
				"-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers",
				"-I.",
				"-I/usr/local/include",
				"-I/usr/local/opt/openssl/include", 
				"-I/usr/local/opt/sqlite/include",
				"-I/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/include/python3.7m",
				"-c",
				cppfile, 
				"-o", 
				ofile,
				"-std=c++11"
			]
			subprocess.run(commands)
			print(" ".join(commands))
			return ofile
		elif self.PlatformsName == "Windows":
			pass




		else:
			exit()



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
				ofile,
				"-o",
				sofile
			]
			print(" ".join(commands))
			subprocess.run(commands)
			return sofile
		elif self.PlatformName == "Darwin":
			sofile = "{}.so".format(ofile.split(".o")[0])
			commands = [
				"clang++",
				"-bundle",
				"-undefined",
				"dynamic_lookup",
				"-isysroot",
				"/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk",
				ofile,
				"-L/usr/local/lib",
				"-L/usr/local/opt/openssl/lib",
				"-L/usr/local/opt/sqlite/lib",
				"-o",
				sofile
			]
			print(" ".join(commands))
			subprocess.run(commands)
			return sofile
		
		elif self.PlatformName == "Windows":
			pass




		else:
			exit()



	def ctypes(self,cppfile):
		ofile = self.ctypes_cpp2o(cppfile)
		sofile = self.ctypes_o2so(ofile)
		print("[ctypes] {} --> {} --> {}".format(cppfile,ofile,sofile))








	
	













		