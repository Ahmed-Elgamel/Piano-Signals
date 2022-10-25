# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:10:53 2022

@author: ahmed
"""



import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

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
#plt.plot(t,song)
#sd.play(song,3*1024)


















N=3*1024

f=np.linspace(0,512,int(N/2))  #axis of the forier transform

x_f=fft(song)
x_f=2/N*np.abs(x_f[0:np.int(N/2)])   #real part of the forier transform of my song

fn1,fn2=np.random.randint(0,512,2)  #random noise frequency
n_t=np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t)  #the noise function

Xn_t=song+n_t   #the noise function added to my song

 
Xn_f=fft(Xn_t)  #fourier transform of the song added to the noise
Xn_f=2/N*np.abs(Xn_f[0:np.int(N/2)]) #the real part of the transform of the funtion that contains noise+song

max_of_forier_transform_of_song=max(x_f) #max of my song in frequency domain


array_of_indices_of_max=[]
for i in range(0,len(Xn_f),1):
    if (Xn_f[i])>np.ceil(max_of_forier_transform_of_song):  #if at this index of the (song+noise)>max of original song
        array_of_indices_of_max.append(i)
        
        
        
fn1_detected=np.round(f[array_of_indices_of_max[0]])
fn2_detected=np.round(f[array_of_indices_of_max[1]])



    
x_filtered=Xn_t-np.sin(2*np.pi*fn1_detected*t)-np.sin(2*np.pi*fn2_detected*t) #my song with noise subtracted from the detected noide frequencies
x_filtered_fourier=fft(x_filtered)
x_filtered_fourier=2/N*np.abs(x_filtered_fourier[0:np.int(N/2)])


plt.subplot(3, 2,1)
plt.plot(t, song)

plt.subplot(3, 2,2)
plt.plot(f,x_f)

plt.subplot(3, 2,3)
plt.plot(t,Xn_t)

plt.subplot(3, 2,4)
plt.plot(f,Xn_f)

plt.subplot(3, 2,5)
plt.plot(t,x_filtered)

plt.subplot(3, 2,6)
plt.plot(f,x_filtered_fourier)




sd.play(x_filtered,3*1024)




















