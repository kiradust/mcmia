# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 13:34:52 2016

@author: Kira
"""
import matplotlib.pyplot as plt
from matplotlib import gridspec
from pylab import rcParams
rcParams['figure.figsize'] = 8,8

clcolor='#2095e7'
kcolor='#53b29d'
xcolor='m'
nacolor='#f27a29'
wcolor='#aaaaaa'

def twoaxes(x,y11,y12,y13,y22):
    fig, ax1 = plt.subplots()
    ax1.plot(x,y11,color=clcolor,linestyle='-')
    ax1.plot(x,y12,color=clcolor,linestyle='--')
    ax1.plot(x,y13,color=xcolor,linestyle='-')
    ax2 = ax1.twinx()
    ax2.plot(x,y22,color=wcolor)
    plt.show()
    return
    
def minifig(delta):
    plt.figure()
    gs = gridspec.GridSpec(2, 1, height_ratios=[1.5, 1]) 
    plt.subplot(gs[0])
    plt.plot(delta[0],delta[1],color=clcolor)
    plt.plot(delta[0],delta[2],color=kcolor)
    plt.plot(delta[0],delta[5],'k')
    plt.subplot(gs[1])
    plt.plot(delta[0],delta[6],color=wcolor)
    return
    
def minifigtwoaxes(delta):
    plt.figure()
    gs = gridspec.GridSpec(2, 1, height_ratios=[1.5, 1]) 
    ax0=plt.subplot(gs[0])
    ax0.plot(delta[0],delta[1],color=clcolor)
    ax0.plot(delta[0],delta[2],color=kcolor)
    ax0.plot(delta[0],delta[3],'k')
    ax1=plt.subplot(gs[1])
    #ax0.get_shared_y_axes().join(ax0, ax1)
    ax1.plot(delta[0],delta[4],color=wcolor)
    ax2=ax1.twinx()
    ax2.plot(delta[0],delta[5],color=xcolor)
    return
    
def minithreefig(delta,colour):
    plt.figure()
    gs = gridspec.GridSpec(3,1,height_ratios=[1.5,0.5,0.5])
    plt.subplot(gs[0])
    plt.plot(delta[0],delta[1],color=clcolor)
    plt.plot(delta[0],delta[2],color=kcolor)
    plt.plot(delta[0],delta[3],'k')
    plt.subplot(gs[1])
    plt.plot(delta[0],delta[4],color=wcolor) #volume
    plt.subplot(gs[2])
    plt.plot(delta[0],delta[5],color=colour) #conc X
    plt.show()
    return