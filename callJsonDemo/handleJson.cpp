#include <iostream>
#include "json.hpp"

using json = nlohmann::json;

extern "C"{
	char* handleJson(const char* json_ptr){
		// static 務必需要 output 才能持續存在 !! 
		static std::string output = "{}";
		std::string json_str(json_ptr);
		json j = json::parse(json_str);
		//==========================
		// json 處理
		j["123"] = "CXX";
		j["中文"] = "CXX";
		j["已經傳到C++了"] = 1.38948938498;
		//==========================
		output = j.dump();
		return &output[0];
	}//endhandleJson
};





