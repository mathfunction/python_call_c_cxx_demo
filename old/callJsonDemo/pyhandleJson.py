import json
import ctypes

#====================================================
# 載入函式模組 , 宣告 cxx 函式回傳型態
cxxfunc = ctypes.CDLL("handleJson.so")
cxxfunc.handleJson.argtypes = [ctypes.c_char_p]
cxxfunc.handleJson.restype = ctypes.c_char_p
#====================================================

# python 呼叫 c++. char* handleJson(const char* json_ptr)
def cxxMethod1(d):
	# python : dict -[dumps]-> str -[encode]-> bytes == [c++] ==> -[decode]-> str -[loads]-> dict  
	return json.loads(cxxfunc.handleJson(json.dumps(d).encode('utf-8')).decode("utf-8"))


if __name__ == '__main__':

	#=========================================================
	# 初始
	d = {
		"中文":203,
		"123":20,
		"2304":[
			12,
			13,
			14,
			15,
			16
		],
		"abcsd":{
			"a":1,
			"b":1
		}
	}
	#============================================================
	print(d)
	d = cxxMethod1(d)
	d["PYTHON 後來更新!!"] = 2
	d = cxxMethod1(d)
	print(d)

