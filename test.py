def MonteCarloPiOpt(n=10000000):
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