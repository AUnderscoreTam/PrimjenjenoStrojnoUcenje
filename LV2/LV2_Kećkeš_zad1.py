import numpy as np
import matplotlib.pyplot as plt
numpyarray = np.array([[1,2,3,3,1],[1,2,2,1,1]])
plt.plot(numpyarray[0],numpyarray[1],'b',marker='o',markersize=5)
plt.axis([0,4,0,4])
plt.title('Primjer')
plt.xlabel('x os')
plt.ylabel('y os')
plt.show()