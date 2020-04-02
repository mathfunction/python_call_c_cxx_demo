## Python_Call_C/C++_Demo

這是關於 Python 使用 C/C++ 加速，如何在各作業系統自動化 "手動編譯指令" 範例

主要是使用 platform.system() 偵測作業系統， os.system() 呼叫 command line 編譯器指令(ex: gcc , cl ... ) !!

**詳細實作詳見 compileDIY.py !!!**

由於編譯器 / python版本差異，需要微幅修改 commands !!

- 舉例:  -fstack-protector-strong , -Wdate-time ，在 gcc >= 4.9 才存在 ，也可看出 python 版本是 3.6 !!

  ```python
  commands = [
  			"gcc",
  			"-pthread",
  			"-DNDEBUG",
  			"-g",
  			"-fwrapv",
  			"-O2",
  			"-Wall",
  			"-g",
  			#"-fstack-protector-strong",
  			"-Wformat",
  			"-Werror=format-security",
  			#"-Wdate-time",
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
  ```

  

- cython 

  - 編譯器範例

  | 作業系統    | c/c++ 編譯器                             |
  | ----------- | ---------------------------------------- |
  | Linux       | [GNU gcc/g++](https://gcc.gnu.org/)      |
  | Mac(Darwin) | [clang/clang++](https://clang.llvm.org/) |
  | Windows     | [MSYS2 gcc/g++](https://www.msys2.org/)  |

  - 函式說明 : 

    ```python
    def cython_copy2pyx(pyfile,source)  # 把 source/XXX.py 複製後變成 ./XXX.py 並改名為 XXX.pyx
    def cython_c2o(cfile)               # 把 ./XXX.c 編譯成 ./XXX.o
    def cython_o2so(ofile)              # 把 ./XXX.o 編譯成 ./XXX.so or ./XXX.pyd
    def cython_compile(pyfile,source)   # 以上函式串聯。XXX.py ---> ./XXX.so or ./XXX.pyd 的流程
    
    # 註:  XXX.py ---> XXX.c 可以用 cython -3 XXX.py 指令處理 !!
    ```

    

- ctypes

  - 編譯器範例

  | 作業系統    | c/c++ 編譯器                                                 |
  | ----------- | ------------------------------------------------------------ |
  | Linux       | [GNU gcc/g++](https://gcc.gnu.org/)                          |
  | Mac(Darwin) | [clang/clang++](https://clang.llvm.org/)                     |
  | Windows     | [MSVC(Microsoft Visual Studio) cl](https://docs.microsoft.com/zh-tw/cpp/build/reference/compiler-options?view=vs-2019) |

  - 函式說明 :

    ```python
    def ctypes_cpp2o(cppfile) # 把 ./XXX.cpp 編譯成 ./XXX.o
    def ctypes_o2so(ofile)    # 把 ./XXX.o 編譯成 ./XXX.so (註: Linux , Darwin 限定)
    def ctypes_compile(cppfile) # 串聯以上函式 ./XXX.cpp ---> ./XXX.so , ./XXX.dll
    ```



- 要加速的程序原始碼:

  pythonFunc.py , cxxFunc.cpp ，裡面分別會跑兩個函式 MonteCarloPi , Floyd_Warshall !!

- 執行範例碼:  詳見 main.py

```bash
# 執行 python 
python3 main.py --run-python 
 
# 編譯 cython
python3 main.py --compile-cython
# 執行 cython  讀取 (.so,.pyd)
python3 main.py --run-cython

# 編譯 ctypes  
python3 main.py --compile-ctypes
# 執行 ctypes 讀取 (.so,.dll)
python3 main.py --run-ctypes
```



- 執行效率 : 

  - macOS High Sierra 10.13.6 / 2.3 GHz Intel Core i5 

  - Apple LLVM version 10.0.0 (clang-1000.11.45.5) 

  - Python 3.7.4

  | 執行指令     | 效率           |
  | ------------ | -------------- |
  | --run-python | 9149.32906 ms  |
  | --run-cython | 5988.693455 ms |
  | --run-ctypes | 192.618996 ms  |

  

##### 編譯器 command line option / ctypes 其他參考:

- GNU gcc  <https://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html#Invoking-GCC>
- clang <https://clang.llvm.org/docs/ClangCommandLineReference.html#diagnostic-flags> 
- MSVC <https://github.com/MicrosoftDocs/cpp-docs/blob/master/docs/build/reference/compiler-options.md>

- ctypes https://docs.python.org/3/library/ctypes.html
- c-cpps Notes https://caiorss.github.io/C-Cpp-Notes/











