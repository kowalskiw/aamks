import matplotlib
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 12})
from navmesh import NavMesh as nm
import numpy as np
import time


df = read_csv('k.csv', delimiter=';')
#print(df['x1'])
points=list()
for i in range(len(df['x1'])):
    points.append((int(df['x1'][i]*100), int(df['y1'][i]*100)))
    points.append((int(df['x2'][i]*100), int(df['y2'][i]*100)))
    points.append((int(df['x3'][i]*100), int(df['y3'][i]*100)))

points = list(set(points))
tri_list = list()
for i in range(len(df['x1'])):
    x = [points.index((int(df['x1'][i]*100), int(df['y1'][i]*100))), points.index((int(df['x2'][i]*100),
                       int(df['y2'][i]*100))),points.index((int(df['x3'][i]*100), int(df['y3'][i]*100)))]
    tri_list.append(x)


x, y = zip(*points)
plt.triplot(x, y, tri_list, linewidth=1.0)
plt.plot(x,y, 'o', ms=2)

n = nm(points=points, triangles=tri_list)

print(n.portals)
origin = (-450.0, -450.0)
plt.plot(origin[0], origin[1], 'o')
n.origin = origin
target= (174.0, 286.0)
#target= (1039.0, 1509.0)
time_s = time.time()
starts = n.find_closest_edge(origin)
shx = n.find_shortest_path(origin=origin, target=target, midpoinds=starts)
n.mid_points = shx
portals = n.order_portals(shx)
n.portals_n = n.portals
## portals.append(tuple([tuple(n.mid_points[-1]), tuple(n.mid_points[-1])]))
left = []
right = []
for i in portals:
    left.append(i[0])
    right.append(i[1])
funnel = n.funnel(portals, origin)
print("TIME:", time.time() - time_s)

x, y = zip(*funnel)
plt.plot(x, y, linewidth=1.0, color='m')
x, y = zip(*shx)
plt.plot(x, y, linewidth=1.0, color='r')
x, y = zip(*left)
plt.plot(x, y, linewidth=1.0, color = 'y')
x, y = zip(*right)
plt.plot(x, y, linewidth=1.0, color = 'black')
#
#plt.xticks(np.arange(1000, 4500, 100))
#plt.yticks(np.arange(0, 2000, 100))
#plt.grid(True)
#plt.savefig('nav.eps', format='eps')
plt.show()
