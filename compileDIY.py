"""===============================================================================================================================================================
	
	這是關於 Python 使用 C/C++ 加速系列:

		
		- compiler 預設 :
			Linux :  
				GNU gcc/g++ - https://gcc.gnu.org/

			Max(Darwin) : 
				clang/clang++ - https://clang.llvm.org/
			Windows :  
				[cython]  MSYS2 gcc.exe (anaconda default) - https://www.msys2.org/
				[ctypes]  MSVC : cl.exe - https://docs.microsoft.com/zh-tw/cpp/build/reference/compiler-options?view=vs-2019
	
		- commands 部分實作，需自行連結函式庫 !! 
		


		- flag options 說明連結 




============================================================================================================================================================="""
import os 
import platform
import shutil

PLATFORM_NAME = platform.system()
	
		

#======================================================================================================================================================================================================================
# cython
def cython_copy2pyx(pyfile,source):
	pyfilename1 = "{}{}".format(source,pyfile)
	pyfilename2 = pyfile
	shutil.copyfile(pyfilename1,pyfilename2)
	pyfilename3 = pyfilename2.split(".py")[0]+".pyx"
	try:
		os.remove(pyfilename3)
		print("remove {}".format(pyfilename3))
	except:
		pass
	os.rename(pyfilename2,pyfilename3)
	print("copy + rename {} to {} !!".format(pyfilename1,pyfilename3))
	return pyfilename3


def cython_c2o(cfile):
	if PLATFORM_NAME == "Linux":
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
		os.system(" ".join(commands))
		return ofile 

	elif PLATFORM_NAME == "Darwin":
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
		os.system(" ".join(commands))
		return ofile
		
	elif PLATFORM_NAME == "Windows":
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
		os.system(" ".join(commands))
		return ofile
	else:
		exit()


def cython_o2so(ofile):
	if PLATFORM_NAME == "Linux":
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
		os.system(" ".join(commands))
		return sofile	
	elif PLATFORM_NAME == "Darwin":
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
		os.system(" ".join(commands))
		return sofile	
	elif PLATFORM_NAME == "Windows":
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
		os.system(" ".join(commands))
		return pydfile
	else:
		exit()
		

def cython_compile(pyfile,source="../python/"):
	pyxfile = cython_copy2pyx(pyfile,source=source)
	os.system(" ".join(["cython","-3",pyxfile])) # python3
	cfile = pyfile.split(".py")[0]+".c"
	ofile = cython_c2o(cfile)
	sofile = cython_o2so(ofile)
	print("[cython_compile] {} --> {} --> {} --> {} --> {}".format(pyfile,pyxfile,cfile,ofile,sofile))


	

	


#======================================================================================================================================================================================================================
# ctypes 系列
def ctypes_cpp2o(cppfile):
	if PLATFORM_NAME == "Linux":
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
		os.system(" ".join(commands))
		return ofile
	elif PlatformsName == "Darwin":
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
		os.system(" ".join(commands))
		return ofile

	else:
		exit()



def ctypes_o2so(ofile):
	if PLATFORM_NAME == "Linux":
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
		os.system(" ".join(commands))
		return sofile
	elif PLATFORM_NAME == "Darwin":
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
		os.system(" ".join(commands))
		return sofile
		
	else:
		exit()



def ctypes_compile(cppfile):
	# 啟動 msvc x86_64  
	if PLATFORM_NAME == "Windows":
		os.system("C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\bin\\x86_amd64\\vcvarsx86_amd64.bat")
		dllfile = "{}.dll".split(cppfile.split(".cpp"))[0]
		commands = [
			"cl",
			"/std:c++14", 
			"/EHsc", 
			"/D_ITERATOR_DEBUG_LEVEL=0", 
			"/O2",
			cppfile,
			#"/I",
			#/link,
			#/libpath:,
			#/DLL,
			"/OUT:",
			dllfile
		]
		os.system(" ".join(commands))
		print("[ctypes_compile] {} --> {} ".format(cppfile,dllfile))
	else:
		ofile = ctypes_cpp2o(cppfile)
		sofile = ctypes_o2so(ofile)
		print("[ctypes_compile] {} --> {} --> {}".format(cppfile,ofile,sofile))








	
	













		