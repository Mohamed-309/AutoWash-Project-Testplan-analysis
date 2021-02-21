import matplotlib.pyplot as plt
x = [0,5,10,15]
y = [3001,2150.35,1554.43,1204.17]
ax = plt.axes()

plt.xlabel("Time (Minutes)")
plt.ylabel("Total Suspended Solids (NTU)")

plt.plot(x,y, color = "skyblue" )
ax.patch.set_alpha(1.0)

plt.show()