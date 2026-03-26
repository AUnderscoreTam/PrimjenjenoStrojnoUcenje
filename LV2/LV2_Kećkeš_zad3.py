import numpy as np
import matplotlib.pyplot as plt


img = plt.imread("tiger.png")
print(img.shape)
print(img.dtype)
img = img[:, :, 0]
plt.figure()
# 90 stupnjeva u smjeru kazaljke na satu
plt.imshow(np.rot90(img), cmap="gray")
# zrcaljenje
np.flip(img, 1)
plt.imshow(np.flip(img, 1), cmap="gray")
# smanjenje
smallnessMultiplier = 5
imgSmall = img[::smallnessMultiplier, :: smallnessMultiplier]
plt.imshow(imgSmall, cmap="gray")
# prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti crni.
first = np.shape(img)
firstD = int(first[1]/4)
img[:, :firstD] = 0
img[:, firstD*2:] = 0
plt.imshow(img, cmap="gray")
plt.show()
