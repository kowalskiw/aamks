from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
from navmesh import NavMesh as nm

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
plt.triplot(x, y, tri_list, linewidth=3.0)
plt.plot(x,y, 'o')
#plt.show()

n = nm()
n.points = points
n.calculate_portals(tri_list)
n.add_portals_to_graph()
origin = (63.0, 216.0)
plt.plot(origin[0], origin[1], 'o')
n.origin = origin
#target= (-305.0, -323.0)
target= (-495.0, 316.0)
#starts = n.find_closest_edge(origin, tri_list)
starts = [(64.0, 216.0)]
shx = n.find_shortest_path(origin=origin, target=target, midpoinds=starts)
n.mid_points = shx
portals = n.order_portals(shx)
n.portals_n = portals
print(portals)
## portals.append(tuple([tuple(n.mid_points[-1]), tuple(n.mid_points[-1])]))
left = []
right = []
for i in portals:
    left.append(i[0])
    right.append(i[1])
funnel = n.funnel(portals, origin)

x, y = zip(*funnel)
plt.plot(x, y, linewidth=3.0, color='m')
x, y = zip(*shx)
plt.plot(x, y, linewidth=3.0, color='r')
x, y = zip(*left)
plt.plot(x, y, linewidth=3.0, color = 'y')
x, y = zip(*right)
plt.plot(x, y, linewidth=3.0, color = 'black')
#
plt.show()
