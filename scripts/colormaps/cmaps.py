import pandas as pd
import matplotlib
import json
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def ansys_colors(n_colours, cmap_):
	norm = matplotlib.colors.Normalize(vmin=1, vmax=n_colours)
	ints = list(range(1, n_colours + 1))
	ints.reverse()
	cs = []
	for i in ints:
		rgb = cmap_(norm(i))
		cmap = matplotlib.colors.to_hex(rgb)
		myval = myfunc(rgb)
		cs.append(myval)
	return cs

def myfunc(rgb):
	rgb256 = [int(i*255) for i in rgb]
	res = rgb256[0] + rgb256[1]*256 + rgb256[2]*256*256
	return res
df = pd.read_csv("scripts/colormaps/fast.csv", header=None).sort_index(ascending=False).reset_index(drop=True)
df = df.astype(float)
fasts = {}
df

fasts['fast'] = df
fasts['fast_reds'] = df[:5]
fasts['fast_blues'] = df[4:]
fasts['fast_blues'][0] = fasts['fast_blues'][0]*2
fasts['fast_reds'][0] = fasts['fast_reds'][0]*2-1
fasts['fast_blues']

for key, value in list(fasts.items()):
	new_key = key+"_r"
	df = value.loc[value.index.values[::-1]]
	df[0] = np.abs((df[0]-1)*-1)
	fasts[new_key] = df.sort_values(0)

for key, value in list(fasts.items()):
	fasts[key] = value.sort_values(0)

fast_cmaps = {}
for name, df in fasts.items():
	data = list(df.apply(lambda row: (row[0], tuple(row[1:]/255)), axis=1))
	cmap = LinearSegmentedColormap.from_list(name, data)
	fast_cmaps[name] = cmap

data = {}
for cmap_name, cmap in fast_cmaps.items():
	data[cmap_name] = {}
	for n_colours in range(4,12):
		print(n_colours,cmap)
		data[cmap_name][n_colours] = ansys_colors(n_colours, cmap)

for cmap_name, cmap in matplotlib.colormaps.items():
	data[cmap_name] = {}
	for n_colours in range(4,12):
		data[cmap_name][n_colours] = ansys_colors(n_colours, cmap)

cmapfile = r"cmaps.json"
with open(cmapfile, 'w') as f:
	json.dump(data, f)