# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:28:35 2017

@author: mucs_b
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib  import cm
import pandas as pd
import math
from colour import Color
import random
from pylab import savefig

plt.figure(figsize=(2,1.25))
plt.axis('off')
c = Color(rgb=(0.5,1,0.5))
c.luminance = 0.2

for i in range(1000):
    coordinates = [[x,y] for x, y in np.random.normal(0.5,0.075,(10,2))]
    axes = plt.gca()
    try:
        lum = np.random.normal(0,0.3)
        if c.luminance+lum >= 0 and  c.luminance+lum <= 1:
            c.luminance += lum
        else: 
            c.luminance -= lum
        r = np.random.normal(0,0.0005)
        if c.red+r >= 0 and  c.red+r <= 1:
            c.red += r
        else: 
            c.red -= r
        g = np.random.normal(0,0.0005)
        if c.green+g >= 0 and  c.green+g <= 1:
            c.green += g
        else: 
            c.green -= r        
        b = np.random.normal(0,0.0005)
        if c.blue+b >= 0 and  c.blue+b <= 1:
            c.blue += b
        else: 
            c.green -= r
    except ValueError:
        pass
    try:
        axes.add_patch(Polygon([[x,y] for x,y in coordinates],
                       facecolor= c.hex,
                       alpha = 0.1,
                       closed=False))
    except ValueError:
        pass

savefig('obj1.png', transparent=True)

plt.show()

x = np.random.normal(0.5,0.1,1000)
y = np.random.normal(0.5,0.1,1000)
#x = np.random.random(3000)
#y = np.random.random(3000)

xcenter = np.mean(x)
ycenter = np.mean(y)

Visframe = pd.DataFrame(
    {'x': x,
     'y': y,
    })

    
    
Visframe['xy'] = Visframe['x']+Visframe['y']

#Visframe2 = Visframe.loc[Visframe['xy'] == min(Visframe['xy'].values)].reset_index(drop = True)[:]
Visframe2 = pd.DataFrame(
    {'x': [0.1],
     'y': [0.1],
     'xy':[0.2]
    })
xReached = 0
iPoint = Visframe.sort_values(by ='xy', ascending = True).head(1).reset_index(drop = True)[:]
Visframe3 = Visframe[:]
plt.figure(figsize=(2,1.5))
plt.axis('off')

while len(iPoint) > 0:
    q1 = random.randrange(300, 700,10)/1000
    q2 = random.randrange(300, 700,10)/1000
    Visframe3 = Visframe3.sample(frac=0.99).reset_index(drop=True)
    try:
        c = Color(rgb=(q1, 1, q2))
        #c = Color(rgb=(1, 1, 1))
        c.luminance = random.randrange(100, 101,100)/1000
        #c.saturation = 0.9
        
        try:
            iPoint_offset = iPoint[:]
            if xReached == 0:
                iPoint = Visframe.loc[Visframe['x'] >= iPoint.loc[0]['x']].sort_values(by ='xy', ascending = True).head(1).reset_index(drop = True)[:]
                Visframe2 = Visframe2.append(iPoint).reset_index(drop = True)
                if iPoint.loc[0]['x'] == max(Visframe['x'].values):
                    xReached = 1
            if xReached == 1:
                iPoint = Visframe.loc[Visframe['x'] <= iPoint.loc[0]['x']].sort_values(by ='xy', ascending = False).head(1).reset_index(drop = True)[:]
                Visframe2 = Visframe2.append(iPoint).reset_index(drop = True)
                if iPoint.loc[0]['x'] == min(Visframe['x'].values):
                    xReached = 2
            if xReached == 2:
                iPoint = Visframe.loc[Visframe['y'] <= iPoint.loc[0]['y']].loc[Visframe['xy'] <= iPoint.loc[0]['xy']].sort_values(by ='x', ascending = True).head(1).reset_index(drop = True)[:]
                Visframe2 = Visframe2.append(iPoint).reset_index(drop = True)
            iPoint_offset = iPoint[:]
            Visframe = Visframe.loc[Visframe['x'] != iPoint.loc[0]['x']].loc[Visframe['y'] != iPoint.loc[0]['y']]
        
            axes = plt.gca()
            outline = plt.plot(np.append(Visframe2['x'].values,Visframe2['x'].values[0]),np.append(Visframe2['y'].values , Visframe2['y'].values[0]))
            plt.setp(outline, color='Black', linewidth=0.75,alpha = 0.01)
            
            #plt.scatter(Visframe3['x'].values,Visframe3['y'].values,c = Visframe3['xy'].values, cmap = cm.seismic)
            axes.add_patch(Polygon([[x,y] for x,y in zip(Visframe2['x'].values,Visframe2['y'].values)],alpha = 0.05,closed=True, facecolor= c.rgb))
            
        except KeyError:
            break 
    except ValueError as e: 
        print(str(e),(q1,q2))
savefig('obj2.png', transparent=True)
plt.show()


x = np.random.normal(0.5,0.1,10000)
y = np.random.normal(0.5,0.1,10000)

Visframe3 = pd.DataFrame(
    {'x': x,
     'y': y,
    })
  
r = 50
riter = random.randrange(r*0.0, r*0.2,1)
Col1 = Color('red')
Col2 = Color('green')
Crange = list(Col1.range_to(Col2, r))

plt.figure(figsize=(2,1.25))
plt.axis('off')
for i in range(r):
    inline = plt.plot(Visframe3['x'].values,Visframe3['y'].values)
    plt.setp(inline, color=Crange[riter].rgb, linewidth=0.9,alpha = 0.1)
    Visframe3 = Visframe3.sample(frac=0.75).reset_index(drop=True)
    riter -= 1
savefig('obj3.png', transparent=True)
plt.show()
