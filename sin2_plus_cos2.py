from math import sin, cos, pi
x = pi/4
value = sin(x)**2 + cos(x)**2
print value

v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0*t +0.5*a*t**2
print s, "meters"

a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1sum = a2 + 2*a*b + b2
eq2sum = a2 - 2*a*b + b2
eq1pow = (a + b)**2
eq2pow = (a - b)**2
print "First equation: %g = %g" % (eq1sum, eq1pow)
print "Second equation: %g = %g" % (eq2sum, eq2pow)
