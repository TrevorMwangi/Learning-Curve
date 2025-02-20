import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file('ne_110m_admin_0_countries.shp')
world.plot(edgecolor='pink')
plt.title("World Map")
plt.show()