# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:39:13 2022

@author: ahmed
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

t=np.linspace(0,3,12*1024)

lefthand=np.array([130.81,146.83,164.81,174.61,196,220,246.93])  #all frequencies of the 3rd ocatve
righthand=np.array([261.63,293.66,329.63,349.23,392,440,493.88]) #all frequencies of the 4th ocatave


mysong1=np.array([ lefthand[1],lefthand[3],lefthand[6] ])     #the left hand of my song
mysong2=np.array([ righthand[6],righthand[4],righthand[2] ])  #the right hand of my song
startTime=np.array([0 ,0.5,1])   #the statring durations
endTime=np.array(  [0.5,1,3])    #the ending durations

def generateSongWave():
   x=0
   for i in range(3):
    f1=mysong1[i]     #lefthand
    f2=mysong2[i]     #righthand
    
    time1=startTime[i]  #the starting time
    time2=endTime[i]    #the ending time
    
    y=np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)      #the function
    z=np.where(np.logical_and(t>time1,t<time2),1,0)  
    x+=(y*z)

   return x
    
    
    
song=generateSongWave()
plt.plot(t,song)
sd.play(song,3*1024)