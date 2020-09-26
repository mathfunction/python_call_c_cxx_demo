

#include <iostream>
#include <string>
#include <limits>
#include <unordered_map>
#include <iomanip>








// 由於 ctypes 不直接支援 double **
void Floyd_Warshall_Algorithm(char**keys,double *vals,int size){
	std::unordered_map<char,int> _idV;
	std::unordered_map<int,char> _invIdV;


	double INF = std::numeric_limits<double>::max();
	// create _idV , _invIdV
	for(int i=0;i<size;i++){
		// split to u , v
		std::string e(keys[i]);  
		char u = e[0];
		// note: e[1] = "-"
		char v = e[2];
		if(_idV.find(u)==_idV.end()){
			_idV[u] = _idV.size();
		}//endif
		if(_idV.find(v)==_idV.end()){
			_idV[v] = _idV.size();
		}//endif

		if(_invIdV.find(_invIdV.size())==_invIdV.end()){
			_invIdV[_invIdV.size()] = u; 
		}//endif

		if(_invIdV.find(_invIdV.size())==_invIdV.end()){
			_invIdV[_invIdV.size()] = v; 
		}//endif
	}//endfor
	

	// allocate A 
	int V = _idV.size();
	
	
	double **A = new double*[V];
	for(int i=0;i<V;i++){
		A[i] = new double [V];
		for(int j=0;j<V;j++){
			A[i][j] = INF;
		}//endfor
		A[i][i] = 0.0;
	}//endfor

	
	for(int i=0;i<size;i++){
		std::string e(keys[i]);  
		char u = e[0];
		// note: e[1] = "-"
		char v = e[2];
		A[_idV[u]][_idV[v]] = vals[i];
	}//endfor

	// main algorithm
	for(int k=0;k<V;k++){
		for(int i=0;i<V;i++){
			for(int j=0;j<V;j++){
				if(A[i][j] > A[i][k] + A[k][j]){
					A[i][j] = A[i][k] + A[k][j];
				}
			}//endfor
		}//endfor
	}//endfor

	// print
	
	for(int i=0;i<V;i++){
		std::cout << "[ ";
		for(int j=0;j<V;j++){
			if(A[i][j] == INF){
				std::cout <<  std::setw(3) << " inf";
			}else{
				std::cout <<  std::setw(3) << A[i][j] << ".";
			}//end_else
		}//endfor
		std::cout << "]\n";
	}//endfor
	


	// 釋放記憶體 !! 
	for(int i=0;i<V;i++){
		delete [] A[i];
	}
	delete [] A;
	

}//end_Floyd_Warshall_Algorithm








double MonteCarloPi(int n){
	int count = 0;
	// ===============================
	long long int Xseed0 = 2019;
	long long int Xseed1 = 11;
	const long long int M = 4294967296;
	long long int MMinus = M-1;
	const long long int a = 1664525;
	const long long int c = 101390423;
	//=================================
	for(int i=0;i<n;i++){
		Xseed0 = (a*Xseed0+c)%M;
		Xseed1 = (a*Xseed1+c)%M;
		double U = (double)Xseed0/MMinus;
		double V = (double)Xseed1/MMinus;
		if((U*U + V*V) < 1.0){
			count += 1;
		}//endif
	}//endfor	
	double pi = 4.0*(count)/n;
	return pi;
}//end_MonteCarloPi


//=============================================================================================================================

extern "C"{
	#if defined _WIN32 || defined _WIN64 
		#define DLLEXPORT __declspec(dllexport)
		DLLEXPORT double cMonteCarloPi(int n){
			return MonteCarloPi(n);
		}//end_MonteCarloPi
		DLLEXPORT void cFWA(char **keys,double *vals,int size){
			Floyd_Warshall_Algorithm(keys,vals,size);
		}


	#else
		double cMonteCarloPi(int n){
			return MonteCarloPi(n);
		}
		void cFWA(char **keys,double *vals,int size){
			Floyd_Warshall_Algorithm(keys,vals,size);
		}

	#endif	


}//end_extern_c


//====================================================================================================================================















































