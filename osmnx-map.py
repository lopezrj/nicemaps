# osmnx-map.py
import sys
import osmnx as ox 

x = 12.136389
y = -86.261389
name= "managua"

if __name__ == "__main__":
    if (len(sys.argv) == 4):
        x= float(sys.argv[1])
        y= float(sys.argv[2])
        name= sys.argv[3]
    else:
        print("ERROR: altan parametros")
        sys.exit(0)


# Center of the map  
latitude = x
longitude = y 

center_point = (latitude, longitude)
G = ox.graph_from_point(center_point, dist=15000, retain_all=True, simplify = True, network_type='all')

### Unpack Data

u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)

# Lists to store colors and widths 
roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#a6a6a6" 
            
        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            color = "#676767"
            
        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            color = "#454545"
            
        elif item["length"] > 400 and item["length"] <= 800:
            color = "#bdbdbd"
            linewidth = 0.35
        else:
            color = "#d5d5d5"
            linewidth = 0.45

        if "primary" in item["highway"]:
            linewidth = 0.5
            color = "#ffff"
    else:
        color = "#a6a6a6"
        linewidth = 0.10
            
    roadColors.append(color)
    roadWidths.append(linewidth)



#Limit borders 
north = latitude + 0.03
south = latitude - 0.03
east = longitude + 0.03
west = longitude - 0.03

bgcolor = "#061529"

fig, ax = ox.plot_graph(G, node_size=0, bbox = (north, south, east, west),
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig(name+".png", dpi=300, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=False)