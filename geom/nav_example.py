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
plt.show()

n = nm()
n.points = points
n.calculate_portals(tri_list)
n.add_portals_to_graph()
origin = (-431.0, -368.0)
target= (-495.0, 443.0),
print(n.portals)
#starts = n.find_closest_edge(origin, tri_list)
shx = n.find_shortest_path(origin=origin, target=target, midpoinds=starts)
#
