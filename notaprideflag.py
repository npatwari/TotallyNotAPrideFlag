#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as plt 
import matplotlib.colors
import matplotlib
matplotlib.rc('xtick', labelsize=14) 
matplotlib.rc('ytick', labelsize=14) 
plt.ion()

# Plot z = y, which is fabulous
plt.figure(1)
cm1 = matplotlib.colors.LinearSegmentedColormap.from_list("", \
        ["#760089","#0044ff","#00811f","#ffef00","#ff8c00","#e70000","#784e18","#000000"])
z   = numpy.fromfunction(lambda y, x: y, (8, 13))
plt.imshow(z, interpolation='nearest', cmap=cm1, origin='lower')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('z=y', fontsize=14)

# Plot z = |y-2|, which is also fabulous
plt.figure(2)
cm2 = matplotlib.colors.LinearSegmentedColormap.from_list("", \
      ["#FFFFFF","#FFFFFF","#F7A8B8","#F7A8B8","#55CDFC","#55CDFC"]) 
z   = numpy.fromfunction(lambda y, x: abs(y-2), (5, 9))
plt.imshow(z, interpolation='nearest', cmap=cm2, origin='lower')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('z=|y-2|', fontsize=14)