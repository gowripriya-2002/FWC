import numpy as np
from cvxpy import *
import matplotlib.pyplot as plt
import subprocess
import shlex

#Parabola parameters
P = np.array([2,4]).reshape(2,-1)
V = np.array([[1,0],[0,0]])
u = np.array([0,-1]).reshape(2,-1)

x = Variable((2,1))

#Cost function
f =  quad_form(x-P, np.eye(2))
obj = Minimize(f)

#Constraints
constraints = [quad_form(x,V) + u.T@x <= 0]

#solution
a=Problem(obj, constraints).solve()
print(np.sqrt(f.value),x.value)

#For plotting 

x = np.linspace(-10,10,100)
y = (x**2)/8
P = np.array([2,4])
Q = np.array([4,2])

ax=plt.plot(x,y)
plt.grid()
plt.axis('equal')


bx=plt.scatter(Q[0],Q[1])
plt.text(Q[0]+0.1,Q[1]+0.1,"Q")
plt.scatter(P[0],P[1])
plt.text(P[0]+0.1,P[1]+0.1,"P")


plt.legend(['$y = x^2/8$'])
plt.savefig('/sdcard/Download/codes/ad_opt_assignment/aopp.pdf')
subprocess.run(shlex.split("termux-open  'storage/emulated/0/Download/codes/ad_opt_assignment/aopp.pdf'"))
#plt.show()
