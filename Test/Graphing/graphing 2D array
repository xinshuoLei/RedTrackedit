import numpy as np
from bokeh.plotting import figure, show

a = np.array([[1,2], [3, 4]])
p = figure(x_range=(0, 2), y_range=(0, 2))

# must give a vector of image data for image parameter
p.image(image=[a], x=0, y=0, dw=2, dh=2, palette="Spectral11")

show(p)