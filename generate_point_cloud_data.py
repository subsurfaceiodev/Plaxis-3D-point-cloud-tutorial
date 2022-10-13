# https://docs.pyvista.org/index.html
from pyvista import examples

mesh = examples.download_st_helens()
warped = mesh.warp_by_scalar('Elevation')
surf = warped.extract_surface().triangulate()
surf = surf.decimate_pro(0.75)  # reduce the density of the mesh by 75%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(surf.points)  # generate dataframe from surface points
df.columns = ['x', 'y', 'z']  # set dataframe columns names
df['x'] -= df['x'].min()  # shift x data to origin
df['y'] -= df['y'].min()  # shift y data to origin
# export data to tab delimited format without index and headers
df.to_csv('point_cloud_data.txt', sep='\t', index=False, header=False)
# plot raw data for later validation with Plaxis 3D
fig = plt.figure(figsize=(11.7, 8.3), constrained_layout=True)
ax = fig.add_subplot(projection='3d')
ax.scatter(df['x'], df['y'], df['z'], s=0.1)
ax.set_box_aspect((np.ptp(df['x']), np.ptp(df['y']), np.ptp(df['z'])))
ax.azim = -240
fig.savefig('point_cloud_data.png')
