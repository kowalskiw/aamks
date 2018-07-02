from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
from navmesh import NavMesh as nm

df = read_csv('k.csv', delimiter=';')
#print(df['x1'])
points=list()
for i in range(len(df['x1'])):
    points.append((round(df['x1'][i]*100, 0), round(df['y1'][i]*100, 0)))
    points.append((round(df['x2'][i]*100, 0), round(df['y2'][i]*100, 0)))
    points.append((round(df['x3'][i]*100, 0), round(df['y3'][i]*100, 0)))

points = list(set(points))
tri_list = list()
for i in range(len(df['x1'])):
    x = [points.index((df['x1'][i], df['y1'][i])), points.index((df['x2'][i], df['y2'][i])), points.index((df['x3'][i], df['y3'][i]))]
    tri_list.append(x)


x, y = zip(*points)
plt.triplot(x, y, tri_list, linewidth=3.0)
plt.plot(x,y, 'o')
plt.show()

n = nm()
n.points = points
n.calculate_portals(tri_list)
n.add_portals_to_graph()
origin = (4, -3)
target= (-4.607115, -4.6842695),
print(n.portals_with_centres.keys())
#starts = n.find_closest_edge(origin, tri_list)
starts = [(4.392884499999999, -3.3842695)]
shx = n.find_shortest_path(origin=origin, target=target, midpoinds=starts)
#
