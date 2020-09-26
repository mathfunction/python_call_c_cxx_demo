"""
	Floyd-Warshall
"""


import numpy as np








def Floyd_Warshall_Algorithm(E):
	_max = float("inf")
	_idV = {}
	_invIdV = {}
	for e in E:
		tup = e.split("-")
		u = tup[0]
		v = tup[1]
		if u not in _idV:
			_idV[u] = len(_idV)
			_invIdV[len(_invIdV)] = u
		if v not in _idV:
			_idV[v] = len(_idV)
			_invIdV[len(_invIdV)] = v

	A = _max * np.ones((len(_idV),len(_idV)))
	for i in range(len(_idV)):
		A[i,i] = 0.0

	for e in E:
		tup = e.split("-")
		u = tup[0]
		v = tup[1]
		A[_idV[u],_idV[v]] = E[e]

	# main algorithm 
	for k in range(len(_idV)):
		for i in range(len(_idV)):
			for j in range(len(_idV)):
				if A[i,j] > A[i,k] + A[k,j]:
					A[i,j] = A[i,k] + A[k,j]

	return A








def MonteCarloPi(n=1000000):
	count = 0
	Xseed0 = 2019
	Xseed1 = 11
	M = 4294967296
	MMinus = M-1
	a = 1664525
	c = 101390423
	for i in range(n):
		Xseed0 = (a*Xseed0+c)%M
		Xseed1 = (a*Xseed1+c)%M
		U = float(Xseed0)/M
		V = float(Xseed1)/M
		if(U*U+V*V)<1.0:
			count+=1
	pi = 4.0*count/n
	return pi


































