###librerias###
import numpy as np
###Esta es la funcion a maximizar
# out = 1-(0.5 - (s_2./((1.+(0.001.*(x.^2.+y.^2))).^2)))
def fun(X,Y):
	X = X+5
	Y = Y+5
	a = 20
	b = 0.2
	c = 2*3.1415926535
	r1 = -a * np.exp( -b * np.sqrt( ((X**2) + (Y**2))/2 ) )
	r2 = -1 * np.exp( (np.cos(c * X)+np.cos(c * Y))/2 )
	r3 = np.exp(1)
	f = -(r1+r2+a+r3)
	##r1 = (X**2)-( 10 * (np.cos(c*X)) )
	##r2 = (Y**2)-( 10 * (np.cos(c*Y)) )
	##f = -(20+r1+r2)
	return f