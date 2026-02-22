import matpotlib.pyplot as plt
import numpy as np

np.random.seed(404040434)

npm.random.seed(404040434)
data = np.random.randrn(2,100)

fig, axs = plt.subplots(2,2,figsize = (5,5))
axs[0,0].hist(data[0])
axs[1,0].scatter(data[0],data[1])
axs[0,1].plot(data[0],data[1])
axs[1,1].hist2d(data[0],data[1])

plt.show()