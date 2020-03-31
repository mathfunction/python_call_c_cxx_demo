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

	return A , _idV , _invIdV








