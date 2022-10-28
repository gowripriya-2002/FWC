import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
#if using termux
import subprocess 
import shlex
#endif                                        


def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB


r1 =2
r2=3
B=np.array(([0,0]))
e1=np.array(([1,0]))
D=4*e1
theta1 = np.pi/2.5
A = np.array(([r1*np.cos(theta1),r2*np.sin(theta1)]))
E=(B+D-A)
C = (B+D)/2
F=(E+C-B)

m1=np.array(A-B)
m2=np.array(B-C)
m3=np.array(C-A)
m4=np.array(D-E)
m5=np.array(E-F)
m6=np.array(F-D)
m7=np.array(A-D)
m8=np.array(C-F)


#f1 = np.linalg.norm(B-C)
#f2 = np.linalg.norm(C-A)
#e1 = np.linalg.norm(E-F)
#e2 = np.linalg.norm(F-D)
#dp1 = np.dot(m_2/f1,m_3/f2)
#dp2 = np.dot(n_2/e1,n_3/e2)
#an1 = np.arccos(dp1)
#an2 = np.arccos(dp2)
#cp1=np.cross(m_1,n_1)
#cp2=np.cross(m_2,n_2)
#cp3=np.cross(o_1,o_1)

x_BA = line_gen(B,A)
x_AD = line_gen(A,D)
x_DE = line_gen(D,E)
x_BE = line_gen(B,E)
x_BC = line_gen(B,C)
x_AC = line_gen(A,C)
x_FD= line_gen(F,D)
x_EF = line_gen(E,F)
x_CF= line_gen(C,F)

plt.plot(x_BA[0,:],x_BA[1,:])#,label='$Line')
plt.plot(x_AD[0,:],x_AD[1,:])#,label='$Line')
plt.plot(x_DE[0,:],x_DE[1,:])#,label='$Line')
plt.plot(x_BE[0,:],x_BE[1,:])#,label='$Line')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Line')
plt.plot(x_AC[0,:],x_AC[1,:])#,label='$Line')
plt.plot(x_FD[0,:],x_FD[1,:])#,label='$Line')
plt.plot(x_EF[0,:],x_EF[1,:])#,label='$Line')
plt.plot(x_CF[0,:],x_CF[1,:])#,label='$Line')





l1 = np.linalg.norm(A-B)
l2 = np.linalg.norm(D-E)
l3 = np.linalg.norm(B-C)
l4 = np.linalg.norm(E-F)
l5 = np.linalg.norm(A-C)
l6 = np.linalg.norm(D-F)

if ((m1==m4).all() ):
	print(" (i)  Quadrilateral ABED is a parallelogram")
if((m2==m5).all()):
	print(" (ii)  Quadrilateral BEFC is a parallelogram")
if ((m7==m8).all()):
	print(" (iii) AD||CF and AD = CF")
	print(" (iv) Quadrilateral ACFD is a parallelogram")
if ((m3==m6).all()):
	print(" (v)  AC= DF")
if (round(l1,4) == round(l2,4)) and (round(l3,4) == round(l4,4)) and (round(l5,4) == round(l6,4)):
   print(" (vi) Triangle ABC is congruent to Triangle DEF")

tri_coords = np.vstack((A,C,D,E,B,F)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','C','D','E','B','F']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal') 
#if using termux
plt.savefig('/sdcard/Download/codes/line_assignment/fig.pdf')
subprocess.run(shlex.split("termux-open  'storage/emulated/0/Download/codes/line_assignment/fig.pdf'"))
#end if
#plt.show()
