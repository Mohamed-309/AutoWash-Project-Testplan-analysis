import matplotlib.pyplot as plt
import numpy as np
import random
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
plt.style.use('_classic_test_patch')
x = []
y = []
z = []

tss  = [167.33, 155.4, 156.163, 145.76, 160.97, 175.133, 150.334, 148.213, 139.93, 190.43, 192.721, 152.7119, 180.81, 185.004, 182.51, 140.00001]
tds = [18.34, 19.11, 16.90, 18.027, 15.96, 14.99, 17.3, 17.8, 14.90, 20.4, 20.1, 21.3, 19.999, 18.701, 12.903, 12.01]
tds_init = [367.333, 377, 356, 361]
for i in range(1,1000):
  test = np.random.uniform(5.00, 19.5)
  x.append(test)
  y.append(3001 - (test*random.choice(tss)))
  z.append (random.choice(tds_init) - (test*random.choice(tds)))

ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.scatter(x,y,z, c='skyblue', marker='o')
ax.set_xlabel("Chemical quantities")
ax.set_ylabel("Total Suspended Solids (TSS)")
ax.set_zlabel("Total Dissolved Solids (TDS)")
plt.show()

