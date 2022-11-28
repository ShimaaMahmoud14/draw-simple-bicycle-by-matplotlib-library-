import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import*
#-------axis------
x1, x2 =0, 150
y1, y2 = 150,0
plt.axis([x1, x2, y1, y2])
plt.xticks(range(x1, x2, 10))
plt.yticks(range(y1, y2,-10))
plt.grid(True, alpha =.1)
axes = plt.gca()
axes.set_aspect(1)
for i in range(2):
    cr = Circle((40+i*70,70),20,color ='k',fill=False)
    axes.add_patch(cr)
pn = np.array([[50,40],[92,40],[70,70],[40,70]])
poly = Polygon(pn,color ='k',fill=False)
axes.add_patch(poly)
plt.plot([110,80],[70,21],color ='k')
plt.plot([70,45],[70,30],color ='k')
rect = Rectangle((70,20),20,2,facecolor='k', edgecolor ='k')
axes.add_patch(rect)
ell = Ellipse((40,30),20,5,facecolor='k', edgecolor ='k')
axes.add_patch(ell)
for j in range(2):
   for i in range(0,360,45):
       we = Wedge((40+j*70,70),19,20+i,40+i)
       axes.add_patch(we)
plt.show()